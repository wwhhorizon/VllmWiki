# vllm-project/vllm#6421: [Bug]: When using qwen-32b-chat-awq with multi-threaded access, errors occur after approximately several hundred visits.”vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.“

| 字段 | 值 |
| --- | --- |
| Issue | [#6421](https://github.com/vllm-project/vllm/issues/6421) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;quantization |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | True |

## 源证据

### Issue 标题

> [Bug]: When using qwen-32b-chat-awq with multi-threaded access, errors occur after approximately several hundred visits.”vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.“

### Issue 正文摘录

### Your current environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0 Clang version: Could not collect CMake version: version 3.22.1 Libc version: glibc-2.35 Python version: 3.12.2 | packaged by Anaconda, Inc. | (main, Feb 27 2024, 17:35:02) [GCC 11.2.0] (64-bit runtime) Python platform: Linux-5.15.0-73-generic-x86_64-with-glibc2.35 Is CUDA available: N/A CUDA runtime version: 12.1.105 CUDA_MODULE_LOADING set to: N/A GPU models and configuration: GPU 0: NVIDIA A100-PCIE-40GB Nvidia driver version: 535.129.03 cuDNN version: Probably one of the following: /usr/lib/x86_64-linux-gnu/libcudnn.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_adv_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_cnn_train.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_infer.so.8.9.0 /usr/lib/x86_64-linux-gnu/libcudnn_ops_train.so.8.9.0 HIP runtime version: N/A MIOpen runtime version: N/A Is XNNPACK available: N/A...

## 现有链接修复摘要

#27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel to optimize beam search | #53 Refactor attention kernels

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: rrent environment ```text Collecting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubun...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 6: ting environment information... PyTorch version: N/A Is debug build: N/A CUDA used to build PyTorch: N/A ROCM used to build PyTorch: N/A OS: Ubuntu 22.04.3 LTS (x86_64) GCC version: (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 6: [Bug]: When using qwen-32b-chat-awq with multi-threaded access, errors occur after approximately several hundred visits.”vllm.engine.async_llm_engine.AsyncEngineDeadError: Background loop has errored already.“ bug;stale...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: ot/autodl-tmp/miniconda3/envs/llm/lib/python3.10/site-packages/starlette/routing.py", line 758, in __call__ await self.middleware_stack(scope, receive, send) File "/root/autodl-tmp/miniconda3/envs/llm/lib/python3.10/sit...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: uda;operator;quantization build_error;crash env_dependency #27 Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | #29 Memcpy kernel for flash attention | #32 Implement block copy kernel...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#27](https://github.com/vllm-project/vllm/pull/27) | mentioned | 0.45 | Add query stride to multi_query_cached_kv_attention & Add kernel benchmark script | ing a bonded set of # nvlinks ``` ### 🐛 describe the bug frame #27: _pyeval_evalframedefault + 0x53d6 (0x4f34c6 in /root/autodl-tmp/miniconda3/envs/llm/bin/python) frame #28: |
| [#29](https://github.com/vllm-project/vllm/pull/29) | mentioned | 0.45 | Memcpy kernel for flash attention | : /root/autodl-tmp/miniconda3/envs/llm/bin/python() [0x5099ce] frame #29: pyobject_call + 0xb8 (0x50a508 in /root/autodl-tmp/miniconda3/envs/llm/bin/python) frame #30: _pyeval_eva… |
| [#32](https://github.com/vllm-project/vllm/pull/32) | mentioned | 0.45 | Implement block copy kernel to optimize beam search | : /root/autodl-tmp/miniconda3/envs/llm/bin/python() [0x5099ce] frame #32: pyobject_call + 0xb8 (0x50a508 in /root/autodl-tmp/miniconda3/envs/llm/bin/python) frame #33: _pyeval_eva… |
| [#53](https://github.com/vllm-project/vllm/pull/53) | mentioned | 0.45 | Refactor attention kernels | (0x4f0c69 in /root/autodl-tmp/miniconda3/envs/llm/bin/python) frame #53: _pyobject_fastcalldicttstate + 0xcd (0x4f676d in /root/autodl-tmp/miniconda3/envs/llm/bin/python) frame #54 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
