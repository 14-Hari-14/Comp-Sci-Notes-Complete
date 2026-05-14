Date: 2025-11-23
Topics: #rust #basic_programming #low_level_programming 
Link: 
Class: [[RUST]]

---

# Basic Data Types in Rust

Understanding the fundamental data types in Rust.

## Scalar types (single values)

### Integers
- `i32` - signed 32-bit (default for numbers)
- `i64` - signed 64-bit
- `u32` - unsigned 32-bit
- `u64` - unsigned 64-bit

### Floating-point
- `f32` - 32-bit float
- `f64` - 64-bit float (default)

### Boolean
- `true` or `false`

### Character
- `char` - single Unicode character

## Compound types (multiple values)

### Tuples
```rust
let tup = (500, 6.4, 1);
let (x, y, z) = tup;  // destructuring
```

### Arrays
```rust
let arr = [1, 2, 3, 4, 5];
let first = arr[0];
```

## Important notes

- Rust is **statically typed** (types must be known at compile time)
- Type annotations sometimes needed: `let x: i32 = 5;`
- All variables are immutable by default

## Related

- [[Rust Initialization and basics]] - Getting started
- [[Rust Roadmap]] - Learning path

---

## Data Types

Rust has 2 sub classifications for its data types those are
- **Scalar**
- **Compound**

Due to rust being statically typed, that is the compiler should know all data types on compile time

In case of multiple types being allowed on 1 variable we need to provide type annotations

```Rust
 let guess: u32 = guess.parse().expect("not number entered");
```

### Scalar
They are the data types that contain only 1 value examples are 
- int
- float
- bool
- char

Int can have the following types
signed integers: 8, 16, 32, 64, 128, architecture dependent; range: -(2)^(n-1) till (2)^(n-1)
similar for unsigned digits; range: 0 till (2)^(n-1)
### Compound
They are the data type that contain multiple values
- tuple
- array



## Shadowing and Mutability

| Shadowing                                                          | Mutability                                                   |
| ------------------------------------------------------------------ | ------------------------------------------------------------ |
| Creates a new variable which has the same name as the old variable | Changes the same variable to have different values           |
| Allows the developer to change type on new assignment              | Doesnt allow the developer to change types of new assignment |
| Requires the let keyword to understand that shadowing is happening | Doesnt require the let keyword                               |
