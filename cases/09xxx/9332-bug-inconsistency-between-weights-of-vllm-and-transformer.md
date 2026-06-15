# vllm-project/vllm#9332: [Bug]: Inconsistency between weights of vllm and transformer

| 字段 | 值 |
| --- | --- |
| Issue | [#9332](https://github.com/vllm-project/vllm/issues/9332) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;mismatch |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Inconsistency between weights of vllm and transformer

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import torch import vllm from transformers import AutoModelForCausalLM import argparse parser = argparse.ArgumentParser() parser.add_argument( "--pretrain", type=str, default="google/gemma-2-2b-it", help="Path to the LLM model" ) args = parser.parse_args() llm = vllm.LLM( **{ "model": args.pretrain, "trust_remote_code": True, "tensor_parallel_size": 1, "dtype": "bfloat16", "gpu_memory_utilization": 0.5, } ) vllm_model = llm.llm_engine.model_executor.driver_worker.model_runner.model vllm_model_param_keys = set([k for k, v in vllm_model.named_parameters()]) transformer_model = AutoModelForCausalLM.from_pretrained( args.pretrain, trust_remote_code=True, attn_implementation="flash_attention_2", quantization_config=None, torch_dtype=torch.bfloat16, ) transformer_model_param_keys = set([k for k, v in transformer_model.named_parameters()]) all_match = True if not vllm_model_param_keys.issubset(transformer_model_param_keys): print("Parameters in vllm but not in transformer:") diff = vllm_model_param_keys.difference(transformer_model_param_keys) print(len(diff), sorted(list(diff))) all_match = False...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: nt ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import torch import vllm from transformers import AutoModelForCausalLM import argparse parser = argparse.ArgumentParser() parser.add_argument( "--pretrai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: "trust_remote_code": True, "tensor_parallel_size": 1, "dtype": "bfloat16", "gpu_memory_utilization": 0.5, } ) vllm_model = llm.llm_engine.model_executor.driver_worker.model_runner.model vllm_model_param_keys = set([k fo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: weights of vllm and transformer bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ``` import torch import vllm from transformers import AutoModelForCausalLM import argparse pars...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ight', 'model.layers.0.self_attn.v_proj.weight', ...] ``` The similar mismatch occurs for `meta-llama/Llama-3.2-1B-Instruct` as well. ### Before submitting a new issue... - [X] Make sure you already searched for relevan...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;mismatch dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
