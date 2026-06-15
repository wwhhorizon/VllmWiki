# vllm-project/vllm#7464: [Bug]: Gemma-2-2b-it load model hangs by vLLM==0.5.1 on Tesla T4 GPU 

| 字段 | 值 |
| --- | --- |
| Issue | [#7464](https://github.com/vllm-project/vllm/issues/7464) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;quantization |
| 子分类 | env_compat |
| Operator 关键词 | attention;cuda;quantization;triton |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Gemma-2-2b-it load model hangs by vLLM==0.5.1 on Tesla T4 GPU 

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_DO_NOT_TRACK"] = "1" llm = LLM( model="/data/test/gemma2_2b_it_prod", max_model_len = 2048, trust_remote_code = False, block_size = 4, max_num_seqs =2, swap_space = 16, max_seq_len_to_capture = 512, load_format = 'auto', dtype = 'float16', kv_cache_dtype = 'auto', seed = 0, enforce_eager=True, gpu_memory_utilization=0.95, tensor_parallel_size =1, worker_use_ray = False ) ``` when i run above code, load model hangs ```python WARNING 08-13 07:04:00 config.py:1354] Casting torch.bfloat16 to torch.float16. WARNING 08-13 07:04:00 utils.py:562] Gemma 2 uses sliding window attention for every odd layer, which is currently not supported by vLLM. Disabling sliding window and capping the max length to the sliding window size (4096). INFO 08-13 07:04:00 llm_engine.py:169] Initializing an LLM engine (v0.5.1) with config: model='/mnt/posfs/globalmount/gemma-2-2b-it', speculative_config=None, tokenizer='/mnt/posfs/globalmount/gemma-2-2b-it', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=Non...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Gemma-2-2b-it load model hangs by vLLM==0.5.1 on Tesla T4 GPU bug ### Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"]
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: Your current environment ### 🐛 Describe the bug ```python from vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_DO_NOT_TRACK"] = "1" llm = LLM( model="/data/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ce = 16, max_seq_len_to_capture = 512, load_format = 'auto', dtype = 'float16', kv_cache_dtype = 'auto', seed = 0, enforce_eager=True, gpu_memory_utilization=0.95, tensor_parallel_size =1, worker_use_ray = False ) ``` w...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 3: m vllm import LLM, SamplingParams import os os.environ["VLLM_ATTENTION_BACKEND"] = "FLASHINFER" os.environ["VLLM_DO_NOT_TRACK"] = "1" llm = LLM( model="/data/test/gemma2_2b_it_prod", max_model_len = 2048, trust_remote_c...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: /gemma2_2b_it_prod", max_model_len = 2048, trust_remote_code = False, block_size = 4, max_num_seqs =2, swap_space = 16, max_seq_len_to_capture = 512, load_format = 'auto', dtype = 'float16', kv_cache_dtype = 'auto', see...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
