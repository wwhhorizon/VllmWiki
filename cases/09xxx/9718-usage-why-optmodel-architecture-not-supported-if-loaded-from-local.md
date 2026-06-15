# vllm-project/vllm#9718: [Usage]: Why OPTModel architecture not supported if loaded from local?

| 字段 | 值 |
| --- | --- |
| Issue | [#9718](https://github.com/vllm-project/vllm/issues/9718) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | activation_norm;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;multimodal_vlm |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Usage]: Why OPTModel architecture not supported if loaded from local?

### Issue 正文摘录

### Your current environment (The output of `python collect_env.py` is appended at the bottom) ## Question: Why OPTModel architecture not supported if loaded from local? ### Background I am trying to run vllm on an HPC environment, where I cannot access hugging face to download model during inference time so I have to download the modle first, and when doing inference, load the model previously downloaded. ### What I have tried This issue is related to I seperate downloading model and doing inference: - Downloading model: ```python # download_model.py from transformers import AutoModel, AutoTokenizer # download model and tokenizer model = AutoModel.from_pretrained("facebook/opt-125m") tokenizer = AutoTokenizer.from_pretrained("facebook/opt-125m") # assign save path model_save_path = "/work/cse-wangtj/models/opt-125m" # save model and tokenizer tokenizer.save_pretrained(model_save_path) model.save_pretrained(model_save_path) print(f"Model and tokenizer saved to {model_save_path}") ``` It seems that the model has been successfully downloaded: ```shell $ ls /work/cse-wangtj/models/opt-125m config.json model.safetensors tokenizer_config.json version.txt merges.txt special_tokens_map.j...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [Usage]: Why OPTModel architecture not supported if loaded from local? usage ### Your current environment (The output of `python collect_env.py` is appended at the bottom) ## Question: Why OPTModel architecture not supp...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 8: : - Downloading model: ```python # download_model.py from transformers import AutoModel, AutoTokenizer # download model and tokenizer model = AutoModel.from_pretrained("facebook/opt-125m") tokenizer = AutoTokenizer.from...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 5: [Usage]: Why OPTModel architecture not supported if loaded from local? usage ### Your current environment (The output of `python collect_env.py` is appended at the bottom) ## Question: Why OPTModel architecture not supp...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: "num_hidden_layers": 12, "pad_token_id": 1, "prefix": " ", "torch_dtype": "float32", "transformers_version": "4.46.0", "use_cache": true, "vocab_size": 50272, "word_embed_proj_dim": 768 } ``` - Doing inference: I implem...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 2: LM', 'DeepseekV2ForCausalLM', 'ExaoneForCausalLM', 'FalconForCausalLM', 'GemmaForCausalLM', 'Gemma2ForCausalLM', 'GPT2LMHeadModel', 'GPTBigCodeForCausalLM', 'GPTJForCausalLM', 'GPTNeoXForCausalLM', 'GraniteForCausalLM',...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
