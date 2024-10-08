# Introduction to Homotopy Type Theory

**80-518, 80-818 — Spring 2018**

_Note: This webpage is recovered from the internet archive, as the original course page was lost._

- **Meeting time and place:** Tue/Thu 12:00 - 1:20, Baker Hall 150
- **Instructor:** Egbert Rijke (erijke[at]andrew.cmu.edu)
- **Office:** Baker Hall 148
- **Office Hours:** Mon/Wed 5:00 - 6:00, or by appointment

[Course notes](hott_intro_cmu.pdf)

---

## Course Description

Homotopy Type Theory (HoTT) is a new field of mathematics that extends Martin-Löf's dependent type theory by the addition of the univalence axiom and higher inductive types. In HoTT we think of types as spaces, dependent types as fibrations, and of the identity types as path spaces. We will see that many spaces that are familiar to topologists can be represented as higher inductive types, and we will develop the basic theorems and constructions in HoTT to reason about them.

## Course material

We will roughly follow the book _Homotopy Type Theory: Univalent Foundations of mathematics_, of which a PDF is freely available.

Some of the later results of synthetic homotopy theory can only be found in recent research papers. We will also use the PhD thesis of Guillaume Brunerie as a resource.

## Organization

Each session will consist of two parts: a 50 minute lecture and 30 minutes in which students present solutions to exercises provided with the previous lecture. These presentations are intended to be short (roughly 5 minutes) and focused to the problem at hand. Problem sets will be posted below with the lecture synopses.

Students are expected to:

Present a solution when they are asked to do so (usually a week in advance). Graduate students will be asked to present more often than undergraduate students.
Per lecture, either correct a somewhat substantial mistake in the notes and exercises, or hand in a written solution for one exercise of their choice. Written solutions are to be handed in at the start of the next lecture for an A, or at the start of the next lecture after that for a B. Collaborations are encouraged, but solutions must be handed in individually. Presenting students hand in a written solution for the exercise they are asked to present.
Hints for the exercises will be presented by the instructor during office hours, a day before they have to be handed in.

---

## Lectures

### Tuesday 1/16, Lecture 1: Introduction

First class! We give motivation for doing homotopy type theory, and introduce dependent type theory. Notes and exercises

HoTT book: The introduction, and section 1.1

### Thursday 1/18, Lecture 2: The type of natural numbers

The set of natural numbers is the most important object of mathematical study. In homotopy type theory its position of importance is only challenged by that of the identity type. We show how to introduce the natural numbers in dependent type theory. Notes and exercises

HoTT book: sections 1.2, 1.4, 1.9

### Tuesday 1/23, Lecture 3: Inductive types

Many types are introduced as inductive types. The prototypal example of inductive types is the type of natural numbers. We will also introduce the empty type, unit type, disjoint sum, and dependent pair types as inductive types. Notes and exercises

HoTT book: sections 1.3, 1.5, 1.6, 1.7, 1.8

### Thursday 1/25, Lecture 4: Identity types

The Martin-Löf identity type on a type A is a binary relation of types on A that is generated just by reflexivity. The induction principle of identity types can be used to give any type the structure of a higher groupoid. Notes and exercises

HoTT book: sections 1.11, 1.12, 2.1, 2.2

### Tuesday 1/30, Thursday 2/1, Lecture 5: Equivalences

Homotopies in type theory are defined as pointwise identification of maps. Using this notion of homotopy, we define equivalences to be bi-invertible maps, and we characterize the identity type of dependent pair types. Notes and exercises

HoTT book: sections 2.4, 2.7

### Tuesday 2/6, Thursday 2/8, Lecture 6: Contractible types and maps

Contractible types are types with a center of contraction, so that every term can be identified with the center of contraction. Similarly, a contractible map is one that has contractible fibers. We prove a coherence theorem, asserting that a map is contractible if and only if it is an equivalence. Notes and exercises

HoTT book: sections 3.11, 4.4

### Tuesday 2/13, Lecture 7: The fundamental theorem of identity types

The fundamental theorem of identity types describes what one has to do to show that a given type family is fiberwise equivalent to the family of identifications with a fixed starting point. Notes and exercises

HoTT book: sections 4.7, 2.12, 8.9. Look for the `encode-decode method'.

### Thursday 2/15, Lecture 8: The hierarchy of homotopical complexity

Not all types possess interesting homotopical structure. For example, some types have no non-trivial loops, and such types are called sets. We describe Voevodsky's hierarchy of homotopical complexity of types, in which a type is of level n if it has no interesting homotopical structure above level n. Notes and exercises

HoTT book: sections 3.1, 3.3, 7.1, 7.2

### Tuesday 2/20, Thursday 2/22, Lecture 9: Function extensionality

The function extensionality axiom asserts that two functions (of the same type) can be identified if they are homotopic. We show that this axiom is equivalent to the axiom that a dependent product of contractible types is again contractible, and we will begin to explore some of its consequences. Notes and exercises

HoTT book: sections 2.9, 2.15

### Tuesday 2/27, Thursday 3/1, Tuesday 3/6, Lecture 10: Homotopy pullbacks

We have shown in lecture 7 that a fiberwise map between two dependent types over a given base type is a fiberwise equivalence if and only if it induces an equivalence on total spaces. In the more general case where we are given a family P over A, a family Q over B, a map f : A -> B, and a fiberwise map g(x) : P(x) -> Q(f(x)) we can give a similar characterization: g is a fiberwise equivalence if and only if it induces a pullback square. Notes and exercises

HoTT book: does not have an introduction to pullbacks.

### Thursday 3/8, Lecture 11: The univalence axiom

The univalence axiom is a type extensionality principle, for types in the universe. It provides an identification between any two equivalent types. Among other things, we show that the univalence axiom implies the function extensionality axiom. Notes and exercises

HoTT book: 2.10, 4.8, 9.8, 10.1

### Tuesday 3/13, Thursday 3/15: Spring break

### Tuesday 3/20, Thursday 3/22, Lecture 12: The circle

In many constructions in mathematics, one can define an object by declaring its generators and its relations (which are equations). Thus it is natural to wonder whether one can also define inductive types that have point constructors (generators) and path constructors (relations). We begin to explore this idea by defining the circle as a higher inductive type, and we show that the loop space of the circle is the type of integers. Notes and exercises

HoTT book: sections 6.1, 6.2, 6.4

### Tuesday 3/27, Thursday 3/29, Lecture 13: Homotopy pushouts

Homotopy pushouts are formed by gluing two types together. This process is similar to the formation of a CW-complex in topology. Examples of pushouts include the n-sphere, for any n, which are formed by forming the unit type to itself in a specific way. We introduce homotopy pushouts as higher inductive types, and we show that they possess a universal property that is dual to the universal property of pullbacks. Therefore we will be able to use the theory of pullbacks to prove theorems about pushouts. Notes and exercises

HoTT book: sections 6.2, 6.5, 6.7, 6.8

### Tuesday 4/3, Tuesday 4/10, Lecture 14: Descent

The descent property for pushouts comes in many forms. In its most rudimentary form it just provides a way of forming type families over pushouts. A more fancy way of stating this is that the pullback of a pushout is again a pushout. In this lecture we will see how these two statements are both closely related to the univalence axiom, and to each other. Notes and exercises

### Thursday 4/5: No class

The instructor will give a talk at the Algebra, Combinatorics, and Geometry seminar at the University of Pittsburgh.

Location: 427 Thackeray Hall  
Time: 12:00pm  

The talk will be aimed at non-experts in HoTT, and all are invited to attend.

### Thursday 4/12, Lecture 15: Sequential colimits

Using higher inductive types one can also form the sequential colimit of a sequence of types. We will study basic properties of sequential colimits, including a descent theorem. Notes and exercises

### Tuesday 4/17, Lecture 16: The homotopy image of a map

The image of a map f : A -> B is an embedding i : im(f) -> B satisfying a universal property, which states essentially that im(f) is the least embedding through which f factors. We show that the image of a map can be constructed as a sequential colimit. Notes and exercises
Thursday 4/19, Carnival

### Tuesday 4/24, Lecture 17: Truncations

If we map a space into a set (i.e. a discrete space), then we see that it always factors through its set of connected components. Therefore the set of connected components of a space X is in a sense the best approximation of X by a discrete space. In type theory we pose a similar question, where the sets get the role of the discrete spaces: Given any type A in the universe, does there exists a k-type A' with a map into it from A, which is in some sense the best k-type approximation of A? We will formulate this precisely by stating a universal property, and use the construction of the image of a map to obtain such a k-type.

### Thursday 4/26, Lecture 18: Homotopy groups of types

We have already seen that the loop space of a 1-type forms a group. The loop space of an arbitrary type doesn't directly form a group, but it does once we 0-truncate it. This is the fundamental group of a type. Similarly, we can also form the higher homotopy groups. We will show that for k>1, the k-th homotopy group of a type is always abelian.
Tuesday 5/1, Lecture 19: The Hopf fibration
The Hopf fibration in HoTT is constructed as a type family over S^2, of which the total space S^3, and fiber S^1. We will also introduce the long exact sequence of homotopy groups, and use it to show that the second homotopy group os S^2 is Z.

### Thursday 5/3, Lecture 26: Open problems in synthetic homotopy theory

Since everything in homotopy type theory must always be homotopy invariant, many constructions in HoTT come with its own set of challenges that are very different than the challenges one meets in classical homotopy theory. For example, there are many classical spaces whose construction in homotopy type theory is unknown. To name a few: the delooping of the 3-sphere, the Grassmannians, the (special) orthogonal groups, and so on. Moreover constructing them in homotopy type theory will inevitably lead to new insights about those spaces, because we can only define them simultaneously with their homotopy types (the type of types merely equal to the constructed type).