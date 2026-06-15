# vllm-project/vllm#19504: [Bug]: Qwen3-GPTQ | Error in inspecting model architecture 'Qwen3MoeForCausalLM'

| 字段 | 值 |
| --- | --- |
| Issue | [#19504](https://github.com/vllm-project/vllm/issues/19504) |
| 状态 | closed |
| 标签 | bug;torch.compile;stale;needs reproduction |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | ci_build;distributed_parallel;model_support;moe;quantization |
| 子分类 | kernel_eff |
| Operator 关键词 | cuda;moe;quantization |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Qwen3-GPTQ \| Error in inspecting model architecture 'Qwen3MoeForCausalLM'

### Issue 正文摘录

### Your current environment **VLLM v 0.9.0.1** ### 🐛 Describe the bug I am using docker image with **VLLM v 0.9.0.1** I have download the model [`Qwen/Qwen3-235B-A22B-GPTQ-Int4`] at this directory `qwen3-gptq`: I have a node with 8 H100 GPUs `VLLM_USE_V1=0 vllm serve qwen3-gptq --tensor-parallel-size 8 --max-model-len 32000 --gpu-memory-utilization 0.9 --distributed-executor-backend mp ` I have this error ``` INFO 06-01 11:19:03 [__init__.py:243] Automatically detected platform cuda. INFO 06-01 11:19:24 [__init__.py:31] Available plugins for group vllm.general_plugins: INFO 06-01 11:19:24 [__init__.py:33] - lora_filesystem_resolver -> vllm.plugins.lora_resolvers.filesystem_resolver:register_filesystem_resolver INFO 06-01 11:19:24 [__init__.py:36] All plugins in this group will be loaded. Set `VLLM_PLUGINS` to control which plugins to load. init_-py:36] All plugins in this group will be loaded. Set "VLLM_PLUGINS' to control which plugins to load. [registry-py: 363] Error in inspecting model architecture 'Qwen3MoeForCausalLM' [registry-py: 363] Traceback (most recent call last): [registry-py: 363] File */usr/local/lib/python3,10/dist-packages/vl]m/model_executor/models/registry-py"...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: | Error in inspecting model architecture 'Qwen3MoeForCausalLM' bug;torch.compile;stale;needs reproduction ### Your current environment **VLLM v 0.9.0.1** ### 🐛 Describe the bug I am using docker image with **VLLM v 0.9....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: **VLLM v 0.9.0.1** I have download the model [`Qwen/Qwen3-235B-A22B-GPTQ-Int4`] at this directory `qwen3-gptq`: I have a node with 8 H100 GPUs `VLLM_USE_V1=0 vllm serve qwen3-gptq --tensor-parallel-size 8 --max-model-le...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Qwen3-GPTQ | Error in inspecting model architecture 'Qwen3MoeForCausalLM' bug;torch.compile;stale;needs reproduction ### Your current environment **VLLM v 0.9.0.1** ### 🐛 Describe the bug I am using docker image...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Qwen3-GPTQ | Error in inspecting model architecture 'Qwen3MoeForCausalLM' bug;torch.compile;stale;needs reproduction ### Your current environment **VLLM v 0.9.0.1** ### 🐛 Describe the bug I am using docker image...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: [Bug]: Qwen3-GPTQ | Error in inspecting model architecture 'Qwen3MoeForCausalLM' bug;torch.compile;stale;needs reproduction ### Your current environment **VLLM v 0.9.0.1** ### 🐛 Describe the bug I am using docker image...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
