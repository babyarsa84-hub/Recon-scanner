# BCUCompSoc Workshop - Python Recon Tool

## Objective

Build a (Expand it, be creative) reconnaissance tool in Python that can:

- Accept an authorised IP address or hostname.
- Scan TCP ports.
- Identify common services from discovered ports.
- Store results in a shared data structure.
- Produce a simple terminal report.
- Work collaboratively using Git/GitHub. https://bcucompsoc.com/sca_git_cheatsheet.pdf

> **Only scan systems you own or have explicit permission to test.**
> For this workshop, use the target provided by the BCUCompSoc/team.

---

## Project structure

```text
recon-tool/
├── main.py
├── recon.py
├── analysis.py
├── report.py
└── README.md
```

### `main.py`
The **coordinator**.

Responsible for:
- Taking the target from the user.
- Creating the shared `results` dictionary.
- Calling the other modules in the correct order.
- Passing the results between stages.

Normally, only the integrator/team lead should need to change this file.

### `recon.py`
The **reconnaissance/scanning** module.

Responsible for:
- TCP port scanning.
- Detecting which ports are open.
- Adding discovered ports to `results`.

Begin with Python's `socket` library.

### `analysis.py`
The **analysis** module.

Responsible for:
- Taking discovered ports.
- Mapping common ports to likely services.
- Adding service information to `results`.

Examples:
- `22` → SSH
- `80` → HTTP
- `443` → HTTPS

### `report.py`
The **reporting** module.

Responsible for:
- Reading the completed `results` dictionary.
- Displaying a clear terminal report.
- It should not perform scanning.

---

## Libraries

### Required

Use Python's standard library only for the core workshop:

- `socket` — TCP connections and port scanning.

You may also use:

- `sys` — command-line/program control if needed.
- `argparse` — optional command-line arguments.
- `json` — optional JSON export.
- `csv` — optional CSV export.
- `datetime` — optional scan timestamps.
- `concurrent.futures` — **advanced extension only**, for concurrent scanning.

Do **not** install third-party packages for the basic version.

The goal is to understand how a basic scanner works before comparing it with professional tools such as Nmap.

---

## Shared data

The modules communicate through one shared `results` dictionary.

The basic structure is:

```text
results
├── target
├── ports
└── services
```

Do not arbitrarily rename these keys.

If your team wants to extend the structure, agree on the change before implementing it.

---

## Team workflow

Each person should primarily own one file.

Example:

| Role | Main file |
|---|---|
| Integrator | `main.py` |
| Recon developer | `recon.py` |
| Analysis developer | `analysis.py` |
| Reporting developer | `report.py` |

Everyone can read the other files, but avoid editing another person's file unless the team has agreed.

Use Git branches for individual work:

```text
main
├── recon-scanning
├── service-analysis
└── reporting
```

Commit your work with a clear message and open a Pull Request when ready.

### Important

Before changing the shared `results` structure, tell the team.

This prevents one module from expecting data that another module no longer produces.

---

## Basic workflow

The finished program should follow:

```text
Target
  ↓
main.py
  ↓
recon.py
  ↓
Open ports added to results
  ↓
analysis.py
  ↓
Services added to results
  ↓
report.py
  ↓
Terminal report
```

---

## Suggested development stages

### Beginner

Get these working first:

1. Accept a target.
2. Scan a small TCP port range.
3. Detect open ports.
4. Store them in `results`.
5. Identify common services.
6. Print a report.

### Advanced extensions

If your group finishes early, consider:

- `argparse` command-line arguments.
- Faster/concurrent scanning with `concurrent.futures`.
- Banner/service identification using `socket`.
- JSON or CSV export.
- Scan timestamps.
- Better error handling.
- Comparing your results with an Nmap scan.
- Adding tests.

Advanced features are optional. Get the basic scanner working first.

---

## Nmap comparison

After building the Python scanner, compare it with Nmap against the same authorised target.

Think about:

- What does your scanner detect?
- What does Nmap detect?
- Why might the results differ?
- What does Nmap provide that your program does not?

The objective is **not** to replace Nmap. It is to understand the fundamentals behind network reconnaissance.

---

## Security and ethics

Only scan:

- Your own systems.
- The BCUCompSoc workshop/lab target.
- Systems where you have explicit permission.

Do not scan random public IP addresses, university infrastructure, or other people's devices.

This is a learning exercise in network reconnaissance.
