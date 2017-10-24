#%%
dataclean = []
def checkio(data) :

    for i in range(len(data)) :

      if data.count(data[i]) >1 :
        dataclean.append(data[i])

    return sorted(dataclean)

#%%
