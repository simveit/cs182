from deeplearning.layers import *
from deeplearning.fast_layers import *


def affine_relu_forward(x, w, b):
    """
    Convenience layer that perorms an affine transform followed by a ReLU

    Inputs:
    - x: Input to the affine layer
    - w, b: Weights for the affine layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    a, fc_cache = affine_forward(x, w, b)
    out, relu_cache = relu_forward(a)
    cache = (fc_cache, relu_cache)
    return out, cache


def affine_relu_backward(dout, cache):
    """
    Backward pass for the affine-relu convenience layer
    """
    fc_cache, relu_cache = cache
    da = relu_backward(dout, relu_cache)
    dx, dw, db = affine_backward(da, fc_cache)
    return dx, dw, db

def affine_relu_batchnorm_forward(x, w, b, bn_param):
    """
    Convenience layer that perorms an affine transform followed by a ReLU followed by a batchnorm

    Inputs:
    - x: Input to the affine layer
    - w, b: Weights for the affine layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    gamma = 1
    beta = 0
    l1, cache1 = affine_relu_forward(x, w, b)
    out, cache2 = batchnorm_forward(l1, gamma, beta, bn_param)
    cache = (cache1, cache2)
    return out, cache

def affine_relu_batchnorm_dropout_forward(x, w, b, bn_param, dropout_param):
    """
    Convenience layer that perorms an affine transform followed by a ReLU followed by a batchnorm

    Inputs:
    - x: Input to the affine layer
    - w, b: Weights for the affine layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    gamma = 1
    beta = 0
    l1, cache1 = affine_relu_forward(x, w, b)
    l2, cache2 = batchnorm_forward(l1, gamma, beta, bn_param)
    out, cache3 = dropout_forward(l2, dropout_param)
    cache = (cache1, cache2, cache3)
    return out, cache

def affine_relu_batchnorm_dropout_backward(dout, cache):
    """
    Backward pass for the affine-relu-batchnorm convenience layer
    """

    cache1, cache2, cache3 = cache
    dl3 = dropout_backward(dout,cache3)
    dl2, _, _ =  batchnorm_backward(dl3, cache2)
    dx, dw, db = affine_relu_backward(dl2, cache1)
    return dx, dw, db


def affine_relu_batchnorm_backward(dout, cache):
    """
    Backward pass for the affine-relu-batchnorm convenience layer
    """

    cache1, cache2 = cache
    dl2, _, _ =  batchnorm_backward(dout, cache2)
    dx, dw, db = affine_relu_backward(dl2, cache1)
    return dx, dw, db

def affine_relu_dropout_forward(x, w, b, dropout_param):
    """
    Convenience layer that perorms an affine transform followed by a ReLU followed by a dropout

    Inputs:
    - x: Input to the affine layer
    - w, b: Weights for the affine layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    l1, cache1 = affine_relu_forward(x,w,b)
    out, cache2 = dropout_forward(l1, dropout_param)
    cache = (cache1, cache2)
    return out, cache

def affine_relu_dropout_backward(dout, cache):
    """
    Backward pass for the affine-relu-batchnorm convenience layer
    """

    cache1, cache2 = cache
    dl2 = dropout_backward(dout, cache2)
    dx, dw, db = affine_relu_backward(dl2, cache1)
    return dx, dw, db


def conv_relu_forward(x, w, b, conv_param):
    """
    A convenience layer that performs a convolution followed by a ReLU.

    Inputs:
    - x: Input to the convolutional layer
    - w, b, conv_param: Weights and parameters for the convolutional layer

    Returns a tuple of:
    - out: Output from the ReLU
    - cache: Object to give to the backward pass
    """
    a, conv_cache = conv_forward_fast(x, w, b, conv_param)
    out, relu_cache = relu_forward(a)
    cache = (conv_cache, relu_cache)
    return out, cache


def conv_relu_backward(dout, cache):
    """
    Backward pass for the conv-relu convenience layer.
    """
    conv_cache, relu_cache = cache
    da = relu_backward(dout, relu_cache)
    dx, dw, db = conv_backward_fast(da, conv_cache)
    return dx, dw, db


def conv_relu_pool_forward(x, w, b, conv_param, pool_param):
    """
    Convenience layer that performs a convolution, a ReLU, and a pool.

    Inputs:
    - x: Input to the convolutional layer
    - w, b, conv_param: Weights and parameters for the convolutional layer
    - pool_param: Parameters for the pooling layer

    Returns a tuple of:
    - out: Output from the pooling layer
    - cache: Object to give to the backward pass
    """
    a, conv_cache = conv_forward_fast(x, w, b, conv_param)
    s, relu_cache = relu_forward(a)
    out, pool_cache = max_pool_forward_fast(s, pool_param)
    cache = (conv_cache, relu_cache, pool_cache)
    return out, cache


def conv_relu_pool_backward(dout, cache):
    """
    Backward pass for the conv-relu-pool convenience layer
    """
    conv_cache, relu_cache, pool_cache = cache
    ds = max_pool_backward_fast(dout, pool_cache)
    da = relu_backward(ds, relu_cache)
    dx, dw, db = conv_backward_fast(da, conv_cache)
    return dx, dw, db
