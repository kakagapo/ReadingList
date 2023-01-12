# Random notes

This in here are yet to orgainized.

## Borax uses

- In Forge welding as flux
  - mixture with ammonium chloride in welding iron and steel
  - mixed with water when soldering jewellary metals(gold or silver)
- neutron absorber in nuclear reactors
- anti-fungal foot soak
- makes slime when mixed with polyvinyl acetate-based glues, such as Elmer's Glue

## Common fluxes used historically

- sodium carbonate
- potash
- charcoal
- coke
- borax
- lime
- lead sulfide
- iron ore in smelting of copper

## Metal joining processes

- Welding
- Brazing
- Soldering

## Common cleaning agents

- Acetic acid (vinegar)
- Acetone (damages plastics)
- Alcohols like isopropyl alcohol or rubbing alcohol
- Citric acid
- Sodium bicarbonate (baking soda)
- Sodium hydroxide (lye)

## Space propulsion

- source : https://hackaday.com/2021/04/19/space-propulsion-separating-fact-from-science-fiction/ 

## Car engine related

- How turbochargers work ? https://auto.howstuffworks.com/turbo.htm
- https://auto.howstuffworks.com/engine.htm

Engineering Connections: Earthquake Proof Bridge (Richard Hammond) | Science Documentary
Vettiver grass used to make incense and used to stabilize river banks as they have long roots.
That was the inspiration behind driving long steel pipes under the sea bed to prevent ground from disintegrating during an earthquake.
To prevent digging in skis and tobbagans have their fronts curved up.
Bridges pylons should not dig in. They need to be able to move without digging in. It is achieved by increasing the particle size(gravel) on the medium on which the pylons rest.

## Visualization

### Broken Horizontal Bar plot

```python
import matplotlib.pyplot as plt 

#Defining the x and y ranges 
xranges = [(5,5), (20,5),(20,7)] 
yrange = (2,1) 

#Plotting the broken bar chart 
plt.broken_barh(xranges, yrange, facecolors='green') 

xranges = [(5,2), (28,5),(40,2)] 
yrange = (30,1) 
plt.broken_barh(xranges, yrange, facecolors='red') 


plt.xlabel('Sales') 
plt.ylabel('Days of the Month') 
plt.show()
```

### Image watermarking

```python
import numpy as np 
import matplotlib.image as image 
import matplotlib.pyplot as plt 

import pandas as pd 
df = pd.read_csv('income.csv') 
lebron_james = df[df['Name']=='LeBron James']

fig, ax = plt.subplots() 
ax.grid() 
ax.plot('Year','earnings ($ million)', data=lebron_james) 
ax.set_title("LeBron James earnings in US$(millions)") 

img = image.imread('Lebron_James.jpeg')
fig.figimage(img, 60, 40,cmap='ocean', alpha=.2)

plt.show()
```

## Grade school math word problems dataset from OpenAI

https://github.com/openai/grade-school-math

## Kubernetes

### Github org and repos

https://github.com/kubernetes-sigs

### Other interesting link

- https://kubernetes.io/docs/concepts/scheduling-eviction/scheduling-framework/
- https://github.com/kubernetes/enhancements/blob/master/keps/sig-scheduling/624-scheduling-framework/README.md
- [Scaling Kubernetes to 7,500 Nodes](https://openai.com/blog/scaling-kubernetes-to-7500-nodes/)
