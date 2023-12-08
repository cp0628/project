from dtsc5502.version import __version__
import dtsc5502.statistics as stats
import dtsc5502.proabilities.functions as probs

print(__version__)
lst = [1,2,3]

print(stats.descriptive.mean(lst))
print(probs.factorial(4))