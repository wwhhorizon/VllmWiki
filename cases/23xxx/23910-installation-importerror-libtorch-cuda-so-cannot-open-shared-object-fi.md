# vllm-project/vllm#23910: [Installation]: ImportError: libtorch_cuda.so: cannot open shared object file: No such file or directory

| 字段 | 值 |
| --- | --- |
| Issue | [#23910](https://github.com/vllm-project/vllm/issues/23910) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support |
| 子分类 | latency_reg |
| Operator 关键词 | cuda;triton |
| 症状 | build_error;crash;import_error;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Installation]: ImportError: libtorch_cuda.so: cannot open shared object file: No such file or directory

### Issue 正文摘录

### Your current environment ```text (user) user@m3pc:~$ wget https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py --2025-08-29 08:00:13-- https://raw.githubusercontent.com/vllm-project/vllm/main/vllm/collect_env.py Resolving raw.githubusercontent.com (raw.githubusercontent.com)... 185.199.109.133, 185.199.110.133, 185.199.111.133, ... Connecting to raw.githubusercontent.com (raw.githubusercontent.com)|185.199.109.133|:443... connected. HTTP request sent, awaiting response... 200 OK Length: 28526 (28K) [text/plain] Saving to: ‘collect_env.py’ collect_env.py 100%[===================================================>] 27.86K --.-KB/s in 0.06s 2025-08-29 08:00:13 (473 KB/s) - ‘collect_env.py’ saved [28526/28526] (user) user@m3pc:~$ python collect_env.py Collecting environment information... Traceback (most recent call last): File "/home/user/collect_env.py", line 825, in main() File "/home/user/collect_env.py", line 804, in main output = get_pretty_env_info() ^^^^^^^^^^^^^^^^^^^^^ File "/home/user/collect_env.py", line 799, in get_pretty_env_info return pretty_str(get_env_info()) ^^^^^^^^^^^^^^ File "/home/user/collect_env.py", line 574, in get_env_info pip_ver...

## 现有链接修复摘要

#23942 [CI] Add `aiter` to matching list of issue auto labeller for `rocm` tag

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: ImportError: libtorch_cuda.so: cannot open shared object file: No such file or directory installation ### Your current environment ```text (user) user@m3pc:~$ wget https://raw.githubusercontent.com/vllm-p
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 526] (user) user@m3pc:~$ python collect_env.py Collecting environment information... Traceback (most recent call last): File "/home/user/collect_env.py", line 825, in main() File "/home/user/collect_env.py", line 804, i...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: ce .venv/bin/activate (user) user@m3pc:~$ uv pip install -U vllm --torch-backend auto Resolved 126 packages in 4.35s Prepared 126 packages in 62ms Installed 126 packages in 408ms + aiohappyeyeballs==2.6.1 + aiohttp==3.1...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Installation]: ImportError: libtorch_cuda.so: cannot open shared object file: No such file or directory installation ### Your current environment ```text (user) user@m3pc:~$ wget https://raw.githubusercontent.com/vllm-...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: entrypoints/cli/__init__.py", line 3, in from vllm.entrypoints.cli.benchmark.latency import BenchmarkLatencySubcommand File "/home/user/.venv/lib/python3.12/site-packages/vllm/entrypoints/cli/benchmark/latency.py", line...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#23942](https://github.com/vllm-project/vllm/pull/23942) | mentioned | 0.6 | [CI]  Add `aiter` to matching list of issue auto labeller for `rocm` tag | s (searchIn: both) #23911: Should have ROCm label: NO (0 matches) #23910: Should have ROCm label: NO (0 matches) #23905: Should have ROCm label: NO (0 matches) #23900: Should hav |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
