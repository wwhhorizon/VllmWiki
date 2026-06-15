# vllm-project/vllm#17388: [Bug]: Failed to import from vllm._C with ImportError

| 字段 | 值 |
| --- | --- |
| Issue | [#17388](https://github.com/vllm-project/vllm/issues/17388) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;import_error;nan_inf |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Failed to import from vllm._C with ImportError

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I use AMD ROCM. I cloned the main branch. Then I ran: DOCKER_BUILDKIT=1 docker build --build-arg BASE_IMAGE="rocm/vllm-dev:navi_base" -f docker/Dockerfile.rocm -t vllm-rocm . The build is successful. But the generated vllm in the docker image does not work. If I run python -c 'import vllm._C' Then the error: ``` INFO 04-29 12:57:36 [__init__.py:239] Automatically detected platform rocm. WARNING 04-29 12:57:36 [rocm.py:29] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') WARNING 04-29 12:57:36 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') Traceback (most recent call last): File " ", line 1, in ImportError: /usr/local/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d ``` There was no such error with the previous version of Vllm. Here is the output: ```python -c 'import vllm._C' INFO 04-29 1...

## 现有链接修复摘要

#17399 [Bugfix] Fix cutlass_mla_decode() accidentally added to ROCM build

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: [Bug]: Failed to import from vllm._C with ImportError bug ### Your current environment ### 🐛 Describe the bug I use AMD ROCM. I cloned the main branch. Then I ran: DOCKER_BUILDKIT=1 docker build --build-arg BASE_IMAGE="...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: r bug ### Your current environment ### 🐛 Describe the bug I use AMD ROCM. I cloned the main branch. Then I ran: DOCKER_BUILDKIT=1 docker build --build-arg BASE_IMAGE="rocm/vllm-dev:navi_base" -f docker/Dockerfile.rocm -...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ocal/lib/python3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') WARNING 04-29 12:57:36 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: a2079fbd71e4b70974d74f62fd3af10) Target: x86_64-unknown-linux-gnu Thread model: posix InstalledDir: /opt/rocm/llvm/bin Configuration file: /opt/rocm-6.3.1/lib/llvm/bin/clang.cfg``` ### Before submitting a new issue... -...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 2: hon3.12/dist-packages/vllm/_C.abi3.so: undefined symbol: _Z18cutlass_mla_decodeRKN2at6TensorES2_S2_S2_S2_S2_d') WARNING 04-29 12:57:36 [_custom_ops.py:21] Failed to import from vllm._C with ImportError('/usr/local/lib/p...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#17399](https://github.com/vllm-project/vllm/pull/17399) | closes_keyword | 0.95 | [Bugfix] Fix cutlass_mla_decode() accidentally added to ROCM build | FIX #17388 Fixes: ed7a29d9f8b4 ("[NVIDIA] Support Cutlass MLA for Blackwell GPUs (#16032)") |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
