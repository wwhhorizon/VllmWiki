# vllm-project/vllm#6180: [Bug]: Multiprocessing FileNotFound error in triton cache

| 字段 | 值 |
| --- | --- |
| Issue | [#6180](https://github.com/vllm-project/vllm/issues/6180) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;model_support;moe;quantization |
| 子分类 | env_compat |
| Operator 关键词 | cuda;moe;quantization;triton |
| 症状 | build_error;crash |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Multiprocessing FileNotFound error in triton cache

### Issue 正文摘录

### Your current environment Hi, When loading the mistralai/Mixtral-8x22B-Instruct-v0.1 model using the LLM function, I keep running into a FileNotFound error where one VllmWorkerProcess appears to try to access a temporary triton cache file of another VllmWorkerProcess, which doesn't exist. My code ran perfectly fine the first time I ran it with the same LLM, but after I killed the first run and tried to run the same code again, I've been having this error. I was able to load another language model meta-llama/Meta-Llama-3-70B-Instruct using the same code. I've tried clearing triton and python caches, but the error persisted. I wasn't able to find any information about this error online, so I'm reaching out for help. I'd appreciate it very much if anyone could share any ideas for fixing this issue. I've attached the full log below. Thanks, Jing-Jing Li ### 🐛 Describe the bug transformers counterpart, which finished running without an error: ```python model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto") ``` Minimal code that reproduces the error: ```python model = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", dtype="auto", trust_remote_code=True, tokenizer...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: ormation about this error online, so I'm reaching out for help. I'd appreciate it very much if anyone could share any ideas for fixing this issue. I've attached the full log below. Thanks, Jing-Jing Li ### 🐛 Describe th...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: = LLM(model="mistralai/Mixtral-8x22B-Instruct-v0.1", dtype="auto", trust_remote_code=True, tokenizer_mode="auto", tensor_parallel_size=8) ``` Log: ``` INFO 07-06 17:29:56 config.py:698] Defaulting to use mp for
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: environment Hi, When loading the mistralai/Mixtral-8x22B-Instruct-v0.1 model using the LLM function, I keep running into a FileNotFound error where one VllmWorkerProcess appears to try to access a temporary triton cache...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: tokenizer='mistralai/Mixtral-8x22B-Instruct-v0.1', skip_tokenizer_init=False, tokenizer_mode=auto, revision=None, rope_scaling=None, rope_theta=None, tokenizer_revision=None, trust_remote_code=True, dtype=torch.bfloat16...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 3: y: '/home/jingjingl/.triton/cache/071003440889f160321353eb6ba91eac/fused_moe_kernel.cubin.tmp.pid_677_441001', Traceback (most recent call last): (VllmWorkerProcess pid=676) ERROR 07-06 17:30:48 multiproc_worker_utils.p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
