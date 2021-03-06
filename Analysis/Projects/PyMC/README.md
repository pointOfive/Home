
# PyMC Examples

- [Trivariate Regression](https://github.com/pointOfive/Home/tree/master/Analysis#bayes-with-pymc3)
- [Experiemental Design](schwartz_farmersdog.pdf)
- More coming soon...

## Modern Bayesian Analysis
- [Probabilistic Programming](https://docs.pymc.io/)
  - with automatic MCMC posterior sampler construction and no need to manually define
    - Metropolis-Hastings acceptance-rejection criteria
    - Gibbs samplers with derived full conditional distributions
- [Hamiltonian Monte Carlo](https://arxiv.org/abs/1701.02434) (HMC) Posterior Sampling
  - which greatly increases sampling speed
  - the [No-U-Turn Sampler](https://arxiv.org/abs/1111.4246) (NUTS) being a popular/ubiquitous example of HMC
- [Variational Inference](https://www.youtube.com/watch?v=rkV6Wu30x4g)
  - which even further increases speed
  - by optimizing a KL-Divergence target rather than pursuing (MC) integration

## Recent Developments (2019-2020)

- The Bayesian Deep Learning [Research Community](http://bayesiandeeplearning.org/) is becoming increasingly active
- The benefits of [Integration over Optimization](https://arxiv.org/abs/2001.10995) are clearly defined and highly promising
- [ALL Optimization Procedures](https://slideslive.com/38923183/deep-learning-with-bayesian-principles) are now seen as [Bayesian Learning Principle](https://arxiv.org/abs/1906.02506) variants
