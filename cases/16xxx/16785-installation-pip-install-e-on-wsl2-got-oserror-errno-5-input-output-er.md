# vllm-project/vllm#16785: [Installation]: `pip install -e .` on WSL2 Got OSError: [Errno 5] Input/output error: 'hl-smi'

| 字段 | 值 |
| --- | --- |
| Issue | [#16785](https://github.com/vllm-project/vllm/issues/16785) |
| 状态 | closed |
| 标签 | installation;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: `pip install -e .` on WSL2 Got OSError: [Errno 5] Input/output error: 'hl-smi'

### Issue 正文摘录

### Your current environment I am trying to install vllm on WSL2 use `pip install -e .` Got: **OSError: [Errno 5] Input/output error: 'hl-smi'** After some debugging, I found the root cause in setup.py ``` def _is_hpu() -> bool: ....... try: out = subprocess.run(["hl-smi"], capture_output=True, check=True) is_hpu_available = out.returncode == 0 except (FileNotFoundError, PermissionError, subprocess.CalledProcessError): if sys.platform.startswith("linux"): try: output = subprocess.check_output( 'lsmod | grep habanalabs | wc -l', shell=True) is_hpu_available = int(output) > 0 except (ValueError, FileNotFoundError, PermissionError, subprocess.CalledProcessError): pass return is_hpu_available ``` subprocess.run will throw OSError if hl-smi is not installed on WSL2. We can verify it by the simple python code on WSL2: ``` import subprocess if __name__ == "__main__": try: out = subprocess.run(["hl-smi"], capture_output=True, check=True) is_hpu_available = out.returncode == 0 except Exception as e: print(type(e)) ``` ### How you are installing vllm ```sh pip install -e . ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: [Installation]: `pip install -e .` on WSL2 Got OSError: [Errno 5] Input/output error: 'hl-smi' installation;stale ### Your current environment I am trying to install vllm on WSL2 use `pip install -e .` Got: **OSError: [E
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: pip install -e .` on WSL2 Got OSError: [Errno 5] Input/output error: 'hl-smi' installation;stale ### Your current environment I am trying to install vllm on WSL2 use `pip install -e .` Got: **OSError: [Errno 5] Input/ou...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: on WSL2 Got OSError: [Errno 5] Input/output error: 'hl-smi' installation;stale ### Your current environment I am trying to install vllm on WSL2 use `pip install -e .` Got: **OSError: [Errno 5] Input/output error: 'hl-sm...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
