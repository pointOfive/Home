
# TensorFlow + Keras

The upcoming [PyMC4](https://pypi.org/project/pymc4/) releases
move from the discontinued Theano backend to
[TensorFlow-Probability](https://www.tensorflow.org/probability) 
peaked my interest.
But [TFPs](https://github.com/tensorflow/probability)
[Advertisement](https://medium.com/tensorflow/regression-with-probabilistic-layers-in-tensorflow-probability-e46ff5d37baf)
[Video](https://www.youtube.com/watch?v=BrwKURU-wpk)
and [Repo](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/jupyter_notebooks/Probabilistic_Layers_Regression.ipynb)
pushed it over the edge.

- I began by exploring KL divergence and [VAEs](https://github.com/tensorflow/probability/blob/master/tensorflow_probability/examples/vae.py)
(and see also [here](https://medium.com/tensorflow/variational-autoencoders-with-tensorflow-probability-layers-d06c658931b7))
- and working through all the [TF Tutorial and Guide Material](https://www.tensorflow.org/overview)
  - as well as other implementation examples such as [this](http://krasserm.github.io/2019/03/14/bayesian-neural-networks/)
  and those linked [below](README.md#outline--reading-list)
- in order to eventually learned about [Attention](https://www.tensorflow.org/tutorials/text/nmt_with_attention) for [NLP](https://www.youtube.com/watch?v=S27pHKBEp30) (which is an area I'm quite curious about/interested in)

On the way I had a chance to revisit and reconsider some foundational statistics topics: 
- Change of Variables "[Bijectors](https://www.tensorflow.org/probability/api_docs/python/tfp/bijectors/Bijector)" 
  forming the basis of Normalizing Flows Generative Modeling 
- Gaussian Processes as [priors](https://slideslive.com/38922672/invited-talk-functional-variational-bayesian-neural-networks?ref=account-folder-43024-folders) for DNNs and as [DNNs](https://twitter.com/EmtiyazKhan/status/1260842226822680576) themselves


A few things I would like to spend some time on but haven't yet gotten to are
- [More Keras Examples](https://github.com/keras-team/keras/tree/master/examples)
- GANs and Reinforcement learning
  - though the former, as a generative modeling approach, is highly connected to a number of topics I have explored
  - and the latter should be of more interested to me than I've given it as it's an area dominated by Bayesian thinking


## Outline / Reading List

- [Optimization is Bayesian Learning Approximated](https://arxiv.org/abs/1906.02506)
  - As discussed in this [Video](https://slideslive.com/38923183/deep-learning-with-bayesian-principles) from [Mohammad Emtiyaz Khan](https://emtiyaz.github.io/)
- Generative Modeling
  - [VAEs](https://arxiv.org/abs/1312.6114)
    - and some [Notes](https://deepgenerativemodels.github.io/notes/index.html) that help clarify what they're doing
  - [Normalizing Flows](https://arxiv.org/abs/1908.09257)
    - and a great [Lecture](https://www.youtube.com/watch?v=3KUvxIOJD0k), [Blog](https://blog.evjang.com/2018/01/nf1.html), and [Course](https://deepgenerativemodels.github.io/notes/flow/) that explain them
    - [Masked Autoregressive Flows](https://arxiv.org/abs/1705.07057)
- Semi-Supervised Learning
  - using [VAEs](https://arxiv.org/abs/1406.5298)
  - using [Normalizing Flows](https://arxiv.org/abs/1912.13025)
- [LeNet-5](http://yann.lecun.com/exdb/lenet/)
- [Advantages of Bayesian Deep Learning](https://arxiv.org/abs/2001.10995)
  - [Bayes by Backprop](https://arxiv.org/abs/1505.05424)
    - and the key [reference](https://papers.nips.cc/paper/4329-practical-variational-inference-for-neural-networks) therein
  - [Bayesian Dropout](https://arxiv.org/abs/1506.02142)
    - along with some [Concerns](https://www.semanticscholar.org/paper/Risk-versus-Uncertainty-in-Deep-Learning-%3A-Bayes-%2C-Osband/dde4b95be20a160253a6cc9ecd75492a13d60c10) and [Comments](https://www.reddit.com/r/MachineLearning/comments/7bm4b2/d_what_is_the_current_state_of_dropout_as/),
    [ect.](https://www.reddit.com/r/MachineLearning/comments/8w0v9m/d_ian_osband_dropout_posteriors_give_bad/) about them
  - [Randomized Prior Functions](https://arxiv.org/abs/1806.03335)
    - and a [great implementation example](https://gdmarmerola.github.io/intro-randomized-prior-functions/), [etc.](https://gdmarmerola.github.io/risk-and-uncertainty-deep-learning/) about them
  - [Bayes using Batch Normalization](https://arxiv.org/abs/1802.06455)
- [BNN posteriors are probably wrong](https://arxiv.org/abs/1906.09686)
  - [HMC is the gold standard](https://arxiv.org/abs/1701.02434)
    - [NUTS is the gold standard HMC](https://arxiv.org/abs/1111.4246)
- [Bayesian Surprise](https://www.sciencedirect.com/science/article/abs/pii/S0378375802002823)
  - and the key [Berger p-value reference](https://www.jstor.org/stable/2685531) therein