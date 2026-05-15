Date: 2025-11-07
Topics: #rust #basic_programming
Purpose:
Link: 
Class: [[RUST]]

---

# Getting Started with Rust

How to set up and start programming in Rust.

## Installation

1. Visit [rustup.rs](https://rustup.rs/)
2. Follow the installation instructions
3. Verify installation: `rustc --version`

## First Rust Program

```rust
fn main() {
    println!("Hello, World!");
}
```

## Basic concepts

- **Variables**: Use `let` to create variables (immutable by default)
- **Mutability**: Use `mut` to make variables changeable
- **Functions**: Define with `fn` keyword
- **Main function**: Starting point of program

## Example

```rust
fn main() {
    let mut x = 5;
    x = 6;
    println!("x is {}", x);
}
```

## Related notes

- [Basic Data Types in Rust](Basic%20Data%20Types%20in%20Rust.md) - Data types
- [Rust Roadmap](Rust%20Roadmap.md) - Learning path
- See Rust documentation for more details

---

To use local documentation and update:

```shell
rustup update
rustup doc
```
To uninstall use:
```shell
rustup self uninstall
```
## Hello World

```rust
fn main() {
	println!("Hello World!");
}
```
To execute a program via terminal
```bash
rustc main.rs
./main
```
This is the most basic rust program **fn** refers to function **main** is the main function where the execution of all programs begin. 

Or u can also use **cargo run** or **cargo build** for projects using dependencies / import statements

**println!** refers to a macro here more specifically **!** symbolizes a macro. Detailed notes on [[macro]]

### Cargo
Cargo is the package manager used by rust which can also install dependencies, build code, etc.

```bash
cargo new project_name
cd project_name
```
Using cargo creates the following dir structure
/src 
--> main.rs
Cargo.lock
Cargo.toml

Full form of toml = Toms obvious minimal language

Commands related to **Cargo**:
1. **cargo init** = initialize the toml file
2. **cargo build** = generate the build for the project, creates an executable inside the target/debug/ directory
3. **cargo build --release** = generates the build for release this is when the app needs to be released to the user and doesn't need as many changes as during development the executable is inside the target/release/ directory. Use this for bench marking code's running time.
4. **cargo run** = compiles the code and runs it
5. **cargo check** = quickly checks the code for compile time errors but doesn't run it 



