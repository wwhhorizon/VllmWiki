# vllm-project/vllm#16696: [Bug]: Unknown gguf model_type: mixtral

| 字段 | 值 |
| --- | --- |
| Issue | [#16696](https://github.com/vllm-project/vllm/issues/16696) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;operator;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unknown gguf model_type: mixtral

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python import torch from transformers import AutoModelForCausalLM, AutoTokenizer from transformers import GenerationConfig from vllm import LLM, SamplingParams model_weight_path = os.path.join(model_dir,"M-MOE-4X7B-Dark-MultiVerse-UC-E32-24B-D_AU-Q4_k_m.gguf") tokenizer_path = os.path.join(tokenizer_dir,"Mistral-MOE-4X7B-Dark-MultiVerse-Uncensored-Enhanced32-24B") llm = LLM( model = model_weight_path, tokenizer = tokenizer_path, hf_config_path = tokenizer_path, dtype=torch.float16, max_model_len=10000, enforce_eager=True, trust_remote_code=True, # max_num_seqs = 128 ) ``` I'm loading a gguf MoE model like above, but get this error: File ~/miniconda3/envs/risk_inference_py310/lib/python3.10/site-packages/vllm/model_executor/model_loader/loader.py:1350, in GGUFModelLoader._get_gguf_weights_map(self, model_config) 1348 break 1349 if arch is None: -> 1350 raise RuntimeError(f"Unknown gguf model_type: {model_type}") 1351 num_layers = config.num_hidden_layers 1352 name_map = gguf.get_tensor_name_map(arch, num_layers) RuntimeError: Unknown gguf model_type: mixtral ### Before submitting a new issue... - [x] Make sure you already searc...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: stale ### Your current environment ### 🐛 Describe the bug ```python import torch from transformers import AutoModelForCausalLM, AutoTokenizer from transformers import GenerationConfig from vllm import LLM, SamplingParam...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: Unknown gguf model_type: mixtral bug;stale ### Your current environment ### 🐛 Describe the bug ```python import torch from transformers import AutoModelForCausalLM, AutoTokenizer from transformers import Generati...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: nizer = tokenizer_path, hf_config_path = tokenizer_path, dtype=torch.float16, max_model_len=10000, enforce_eager=True, trust_remote_code=True, # max_num_seqs = 128 ) ``` I'm loading a gguf MoE model like above, but get...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: et_gguf_weights_map(self, model_config) 1348 break 1349 if arch is None: -> 1350 raise RuntimeError(f"Unknown gguf model_type: {model_type}") 1351 num_layers = config.num_hidden_layers 1352 name_map = gguf.get_tensor_na...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rallel;frontend_api;hardware_porting;model_support;moe cuda;moe;operator;triton build_error dtype;env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
