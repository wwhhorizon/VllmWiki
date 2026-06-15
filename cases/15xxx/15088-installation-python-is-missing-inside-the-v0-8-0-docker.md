# vllm-project/vllm#15088: [Installation]: python is missing inside the v0.8.0 docker

| 字段 | 值 |
| --- | --- |
| Issue | [#15088](https://github.com/vllm-project/vllm/issues/15088) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Installation]: python is missing inside the v0.8.0 docker

### Issue 正文摘录

### Your current environment just pull the official docker v0.8.0. However the python is missing and all binaries are now located inside /opt/venv/bin/ instead of /usr/local/bin : ls -l /opt/venv/bin/ total 1120 -rwxr-xr-x 1 root root 321 Mar 19 02:29 accelerate -rwxr-xr-x 1 root root 313 Mar 19 02:29 accelerate-config -rwxr-xr-x 1 root root 315 Mar 19 02:29 accelerate-estimate-memory -rwxr-xr-x 1 root root 313 Mar 19 02:29 accelerate-launch -rwxr-xr-x 1 root root 312 Mar 19 02:29 accelerate-merge-weights -rw-r--r-- 1 root root 3685 Mar 19 02:09 activate -rw-r--r-- 1 root root 2648 Mar 19 02:09 activate.bat -rw-r--r-- 1 root root 2592 Mar 19 02:09 activate.csh -rw-r--r-- 1 root root 4156 Mar 19 02:09 activate.fish -rw-r--r-- 1 root root 3841 Mar 19 02:09 activate.nu -rw-r--r-- 1 root root 2762 Mar 19 02:09 activate.ps1 -rw-r--r-- 1 root root 2383 Mar 19 02:09 activate_this.py -rwxr-xr-x 1 root root 296 Mar 19 02:29 ccmake -rwxr-xr-x 1 root root 294 Mar 19 02:29 cmake -rwxr-xr-x 1 root root 294 Mar 19 02:29 cpack -rwxr-xr-x 1 root root 294 Mar 19 02:27 cpuinfo -rwxr-xr-x 1 root root 294 Mar 19 02:29 ctest -rw-r--r-- 1 root root 1728 Mar 19 02:09 deactivate.bat -rwxr-xr-x 1 root roo...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: [Installation]: python is missing inside the v0.8.0 docker installation ### Your current environment just pull the official docker v0.8.0. However the python is missing and all binaries are now located inside /opt/venv/b
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: 02:29 accelerate -rwxr-xr-x 1 root root 313 Mar 19 02:29 accelerate-config -rwxr-xr-x 1 root root 315 Mar 19 02:29 accelerate-estimate-memory -rwxr-xr-x 1 root root 313 Mar 19 02:29 accelerate-launch -rwxr-xr-x 1 root r...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: 19 02:27 gguf-dump -rwxr-xr-x 1 root root 342 Mar 19 02:27 gguf-new-metadata -rwxr-xr-x 1 root root 342 Mar 19 02:27 gguf-set-metadata -rwxr-xr-x 1 root root 292 Mar 19 02:27 httpx -rwxr-xr-x 1 root root 327 Mar 19 02:2...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: 294 Mar 19 02:27 cpuinfo -rwxr-xr-x 1 root root 294 Mar 19 02:29 ctest -rw-r--r-- 1 root root 1728 Mar 19 02:09 deactivate.bat -rwxr-xr-x 1 root root 300 Mar 19 02:27 distro -rwxr-xr-x 1 root root 300 Mar 19 02:27 doten...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
