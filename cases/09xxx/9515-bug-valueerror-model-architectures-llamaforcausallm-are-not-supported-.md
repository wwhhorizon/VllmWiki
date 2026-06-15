# vllm-project/vllm#9515: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. Supported architectures

| 字段 | 值 |
| --- | --- |
| Issue | [#9515](https://github.com/vllm-project/vllm/issues/9515) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;model_support;multimodal_vlm |
| 子分类 | memory |
| Operator 关键词 | cuda |
| 症状 |  |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. Supported architectures

### Issue 正文摘录

### Your current environment ### Model Input Dumps ## vLLM version: 0.6.3.post1 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.161.07 Driver Version: 535.161.07 CUDA Version: 12.2 | |-----------------------------------------+----------------------+----------------------+ | GPU Name Persistence-M | Bus-Id Disp.A | Volatile Uncorr. ECC | | Fan Temp Perf Pwr:Usage/Cap | Memory-Usage | GPU-Util Compute M. | | | | MIG M. | |=========================================+======================+======================| | 0 NVIDIA A100-SXM4-80GB On | 00000000:47:00.0 Off | 0 | | N/A 31C P0 64W / 400W | 0MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ | 1 NVIDIA A100-SXM4-80GB On | 00000000:4E:00.0 Off | 0 | | N/A 31C P0 63W / 400W | 0MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+----------------------+----------------------+ | 2 NVIDIA A100-SXM4-80GB On | 00000000:87:00.0 Off | 0 | | N/A 34C P0 64W / 400W | 0MiB / 81920MiB | 0% Default | | | | Disabled | +-----------------------------------------+--------...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 8: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. Supported architectures bug ### Your current environment ### Model Input Dumps ## vLLM version: 0.6.3.post1 +-----------------------...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 7: ures bug ### Your current environment ### Model Input Dumps ## vLLM version: 0.6.3.post1 +---------------------------------------------------------------------------------------+ | NVIDIA-SMI 535.161.07 Driver Version:...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: [Bug]: ValueError: Model architectures ['LlamaForCausalLM'] are not supported for now. Supported architectures bug ### Your current environment ### Model Input Dumps ## vLLM version: 0.6.3.post1 +-----------------------...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: PU GI CI PID Type Process name GPU Memory | | ID ID Usage | |=======================================================================================| | No running processes fou
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
