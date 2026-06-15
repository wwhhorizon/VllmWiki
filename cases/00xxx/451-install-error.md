# vllm-project/vllm#451: install error

| 字段 | 值 |
| --- | --- |
| Issue | [#451](https://github.com/vllm-project/vllm/issues/451) |
| 状态 | closed |
| 标签 | installation |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel |
| 子分类 | install |
| Operator 关键词 | cuda;triton |
| 症状 | build_error |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> install error

### Issue 正文摘录

when I run pip install vllm==0.1.2, the error occur, what is **ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device？** could you help me ``` Collecting vllm==0.1.2 Downloading https://pypi.tuna.tsinghua.edu.cn/packages/f9/ed/1e4625f290e24c1381aeeb66620b32755b17f2894a4227fb49fb20fa0ec9/vllm-0.1.2.tar.gz (93 kB) ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 93.8/93.8 kB 592.0 kB/s eta 0:00:00 Installing build dependencies ... error error: subprocess-exited-with-error × pip subprocess to install build dependencies did not run successfully. │ exit code: 1 ╰─> [56 lines of output] xxxxx xxxxx xxxx xxx xxxx xxxx ollecting mpmath>=0.19 (from sympy->torch>=2.0.0) Using cached https://pypi.tuna.tsinghua.edu.cn/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl (536 kB) Installing collected packages: ninja, mpmath, lit, cmake, wheel, typing-extensions, sympy, setuptools, packaging, nvidia-nccl-cu11, nvidia-cufft-cu11, nvidia-cuda-nvrtc-cu11, networkx, MarkupSafe, filelock, nvidia-nvtx-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda-cupti-cu11, nvidia-cublas-cu11, jinja2...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: install error installation when I run pip install vllm==0.1.2, the error occur, what is **ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device？** could you help me ``` Collecting vllm
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 11, nvidia-cublas-cu11, jinja2, nvidia-cusolver-cu11, nvidia-cudnn-cu11, triton, torch ERROR: Could not install packages due to an OSError: [Errno 28] No space left on device [end of output] note: This error originates...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ympy, setuptools, packaging, nvidia-nccl-cu11, nvidia-cufft-cu11, nvidia-cuda-nvrtc-cu11, networkx, MarkupSafe, filelock, nvidia-nvtx-cu11, nvidia-cusparse-cu11, nvidia-curand-cu11, nvidia-cuda-runtime-cu11, nvidia-cuda...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
