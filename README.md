# The Mutually Unbiased Bases Library
The purpose of this library is to implement various methods for constructing mutually unbiased bases as well as exporing their applications. This library serves as a sumplement to my masters thesis on the topic.

## Install Instructions
This library requires the current version of NumPy (v2.3), QuTip (v5) and was made in Python (v3.13). QuTip is a custom python library designed for quantum simulations. It can be though of as a wrapper arounf NumPy that adds some nice additional functionality useful for quantum applications. Click for more information about [QuTip](https://qutip.org/) or [NumPy](https://numpy.org/doc/stable/user/whatisnumpy.html).


## The Basis "Data Type"
There are lots of ways to store sets of bases. The most common being lists of square numpy arrays or mxnxn numpy arrays. In this case however, to take advantage of some built-ins from qutip and make some of the applications easier, we want to be able to access each of the column vectors or state-vectors in our set of bases easily. So the standard data-type used for sets of mutually unbiased bases in this library is and nxd numpy array, where n is the number of bases and d is the number of vectors per basis. Each entry in this array is a quantum state of type qutip.QObj.

![mubsdatatype(1)](https://github.com/user-attachments/assets/4f4b17f3-6fce-4081-b9af-74f6fb08f5cc)


For example, in d=4 we can construct a complete set of 5 basis each including 4, 4-d column vectors. This can be unintuitive at first but makes the indexing bases[basis#][state#] and len(bases)= the number of basises.

## Generation Methods
There are a verity of known construction methods for mutually unbiased bases in prime power dimensions. The most unique is conversion of mutually orthogonal latin suqares to mutually unbiased bases. This method and it's associated functions are in it's own file; latin_squares.py. The other construction methods are ways of mapping finite fields to complete sets of mutually unbiased bases. The first of these methods to be developed was published by Wooters and Fields in [ref](). We will use this technique as the default construction method in mubslib.genmubs(). The other construction methods are based largely on the structure layed out in [A New Proof...]() by Band, Boy, Roy and Vatan. In their paper, they prove that by generating classes of commutting matrices, the joint eigen vectors of each class (i.e. the eigen vectors that allow you to simultaneously diagonalize all the matrices in that class) would form a set of mutually unbiased bases. Their construction method goes as follows: finite field -> d+1 classes of d commuting matrices -> solve for the joint eigen values. This process has also been utalized in [ref]() and [ref]() who developed somewhat simpler ways of constructing commuting classes from generalized spin matrices and finite fields repectively. All of these techniques are implemented in functions from fields.py. Finally, in the unitlities there are some simple functions used throughout the code such as mubslibs.ismub(), mubslib.isdiag() and mubslibs.primepowerfactors().
