import numpy as np
def simulate_circular(demand, return_rate=0.6, reuse_rate=0.3, remfg_rate=0.4, recycle_rate=0.25, n_periods=24, seed=42):
    rng=np.random.default_rng(seed); new_prod=[]; reused=[]; remfg=[]; recycled=[]; waste=[]
    inv_new=demand*2; inv_return=0
    for t in range(n_periods):
        d=demand*(1+rng.normal(0,0.1))
        returns=d*return_rate*rng.uniform(0.8,1.2)
        inv_return+=returns
        r_reuse=min(inv_return*reuse_rate,d*0.4); inv_return-=r_reuse
        r_remfg=min(inv_return*remfg_rate,d*0.3); inv_return-=r_remfg
        r_recycle=inv_return*recycle_rate; inv_return-=r_recycle
        r_waste=inv_return*0.1; inv_return=max(0,inv_return-r_waste)
        needed=max(0,d-r_reuse-r_remfg)
        new_prod.append(needed); reused.append(r_reuse); remfg.append(r_remfg)
        recycled.append(r_recycle); waste.append(r_waste)
    virgin_reduction=1-np.sum(new_prod)/(demand*n_periods)
    return {"avg_new_production":round(np.mean(new_prod),0),"avg_reused":round(np.mean(reused),0),
            "avg_remanufactured":round(np.mean(remfg),0),"avg_recycled":round(np.mean(recycled),0),
            "virgin_material_reduction":round(virgin_reduction*100,1),"circularity_index":round((np.sum(reused)+np.sum(remfg)+np.sum(recycled))/(demand*n_periods)*100,1)}
if __name__=="__main__": print(simulate_circular(1000))
