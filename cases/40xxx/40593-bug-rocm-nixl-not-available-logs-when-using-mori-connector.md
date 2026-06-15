# vllm-project/vllm#40593: [Bug][ROCm]: NIXL not available logs when using MoRI connector

| 字段 | 值 |
| --- | --- |
| Issue | [#40593](https://github.com/vllm-project/vllm/issues/40593) |
| 状态 | open |
| 标签 | bug;rocm |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;hardware_porting;model_support;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | fp8 |
| 症状 |  |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug][ROCm]: NIXL not available logs when using MoRI connector

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I am running vLLM with the MoRI-IO connector (standard deployment). However, I get logs about NIXL not being available (as it's not), but since I am not using NIXL I don't really mind if NIXL is available or not. Not an actual issue but more confusion IMO. I would expect these logs not to show up unless we actually use NIXL. ``` WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:46 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:46 [nixl_utils.py:44] NIXL...

## 现有链接修复摘要

#40594 [Fix][ROCm] Suppress irrelevant NIXL logs at import

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 5: s.py:44] NIXL agent config is not available ``` I am running this: ``` docker run -it --rm \ --init \ --network host \ --ipc host \ --privileged \ --cap-add SYS_PTRACE \ --security-opt seccomp=unconfined \ --ulimit meml...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: XL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent config is not available WARNING 04-22 08:08:45 [nixl_utils.py:34] NIXL is not available WARNING 04-22 08:08:45 [nixl_utils.py:44] NIXL agent confi...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: format dummy \ --tensor-parallel-size 8 \ --kv-cache-dtype fp8 \ --gpu-memory-utilization 0.7 \ --max-num-batched-tokens 32768 \ --max-model-len 16384 \ --trust-remote-code \ --no-enable-prefix-caching \ --block-s
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 2: IMEOUT_S=3600 \ -e VLLM_SERVER_DEV_MODE=1 \ -e VLLM_ROCM_USE_AITER=1 \ -e VLLM_ROCM_USE_AITER_PAGED_ATTN=0 \ -e VLLM_ROCM_USE_AITER_RMSNORM=1 \ -e VLLM_USE_AITER_TRITON_SILU_MUL=0 \ ${VLLM_IMAGE} \ deepseek-ai/DeepSeek-...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: [Bug][ROCm]: NIXL not available logs when using MoRI connector bug;rocm ### Your current environment ### 🐛 Describe the bug I am running vLLM with the MoRI-IO connector (standard deployment). However, I get logs about N...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#40594](https://github.com/vllm-project/vllm/pull/40594) | closes_keyword | 0.95 | [Fix][ROCm] Suppress irrelevant NIXL logs at import | Fixes #40593. **Context:** The nixl_utils.py logs warnings upon import if NIXL/RIXL is not available. Currently we always import this utils file from the eplb code paths, even w |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
