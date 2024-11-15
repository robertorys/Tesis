from mib_v2_3_3.mibAp import MibAp
from mib_v2_3_3.mib import Mib
from mib_v2_3_3.specification import Specification
from mib_v2_3_3.specification import Copy
from mib_v2_3_3.distrib import Distrib
from mib_v2_3_3.var import Var
import multiprocessing as mp

class MibMp(Mib):
    
    def __init__(self, description, process_n = 4):
        self.process_n = process_n 
        super().__init__(description)
    
    def process(self, ds: Specification, uknown:set, p:mp.Queue) -> None:
        mib = Mib(ds)
        p.put(mib.probability(uknown))
    
        
    def probability(self, uknown) -> float:
        U = list([Var(v.name, v.values) for v in uknown])
        n2v_U = dict([(v.name, v) for v in U])
        size = len(U) // self.process_n
        
        partitions = [U[i * size:(i + 1) * size] for i in range(self.process_n)]

        # Añadir los elementos restantes (si hay alguno) a las particiones existentes
        for i, extra in enumerate(U[self.process_n * size:]):
            partitions[i].append(extra)
        
        for su in partitions:
            print(f"O:partición:{[v.name for v in su]}")
            for v in su:
                v.event = v.getValues()[0]
                v.values = v.values - set([v.event])
        
        p_q = mp.Queue()
        processes = []
        
        for partition in partitions:
            if len(partition) > 0:
                names = [v.name for v in partition]
                ds_copy, n2v = Copy(self.ds)
                
                uknown_p = set()
                print(f"partición:{[v.name for v in partition]}")
                for v in ds_copy.vars:
                    if not v.name in names and v.name in n2v_U.keys():
                        v.values = n2v_U[v.name].values
                        uknown_p.add(v)
                    elif v.name in names:
                        v.event = n2v_U[v.name].event
                    print(f"{v.name}:({v.event}, {v.values})")
                    
                process = mp.Process(
                    target=self.process,
                    args=(
                        ds_copy,
                        uknown_p,
                        p_q
                    )
                )
                processes.append(process)
            
        for process in processes:
            process.start()
        for process in processes:
            process.join()
                
        p = 0
        while not p_q.empty():
            p += p_q.get()
        return p
    
class MibApMp(MibAp):
    
    def __init__(self, ds, N, process_n = 4):
        self.process_n = process_n
        super().__init__(ds, N)
    
    def direct_sampling(self, ds:Specification, vars:tuple, values:tuple, count_q:mp.Queue, N:int) -> None:
        mib = MibAp(ds,N)
        
        count = mib.direct_sampling(vars, values)
        
        count_q.put(count)
    
    def gibss_sampling(self, ds:Specification, vars:tuple, values:tuple, indep:tuple, indep_v:tuple,count_q:mp.Queue, N:int) -> None:
        mib = MibAp(ds,N)
        
        count = mib.gibss_sampling(vars, values, indep, indep_v)
        
        count_q.put(count)
    
    def marginal(self, vars:tuple, values:tuple) -> float:
        processes = []
        count = mp.Queue()
        for i in range(self.process_n):
            ds_copy, n2v = Copy(self.ds)
            vars_mc = tuple([n2v[v.name] for v in vars])
            
            process = mp.Process(
                target=self.direct_sampling,
                args=(
                    ds_copy,
                    vars_mc, 
                    values, 
                    count,
                    self.N
                )
            )
            processes.append(process)
        
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        
        count_e = 0
        while not count.empty():
            count_e += count.get()
        if count_e == 0:
            return 1 / (self.N * self.process_n)
        return count_e / (self.N * self.process_n)

    def cond(self, vars, values, indep, indep_values):
        processes = []
        count = mp.Queue()
        for i in range(self.process_n):
            ds_copy, n2v = Copy(self.ds)
            
            vars_mc = tuple([n2v[v.name] for v in vars])    
            indep_mc = tuple([n2v[v.name] for v in indep])     
               
            process = mp.Process(
                target=self.gibss_sampling,
                args=(
                    ds_copy,
                    vars_mc, 
                    values, 
                    indep_mc,
                    indep_values,
                    count,
                    self.N
                )
            )
            processes.append(process)
        
        for process in processes:
            process.start()
        for process in processes:
            process.join()
        
        count_e = 0
        while not count.empty():
            count_e += count.get()
        if count_e == 0:
            return 1 / (self.N * self.process_n)
        return count_e / (self.N * self.process_n)