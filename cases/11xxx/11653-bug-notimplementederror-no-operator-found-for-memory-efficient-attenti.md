# vllm-project/vllm#11653: [Bug]: NotImplementedError: No operator found for memory_efficient_attention_forward

| 字段 | 值 |
| --- | --- |
| Issue | [#11653](https://github.com/vllm-project/vllm/issues/11653) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;model_support |
| 子分类 | debug |
| Operator 关键词 | cuda;operator |
| 症状 | build_error |
| 根因提示 | dtype;env_dependency;shape |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: NotImplementedError: No operator found for memory_efficient_attention_forward

### Issue 正文摘录

### Your current environment torch==2.5.1+cu124 xformers==0.0.28.post3 python==3.10 vllm==0.6.4 GPU：A100-80G ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to use **vllm==0.6.4** to accelerate **qwen2-1.5B-instruct** embedding model, while I got this **bug:** ``` NotImplementedError: No operator found for `memory_efficient_attention_forward` with inputs: query : shape=(1, 20394, 2, 6, 128) (torch.float32) key : shape=(1, 20394, 2, 6, 128) (torch.float32) value : shape=(1, 20394, 2, 6, 128) (torch.float32) attn_bias : p : 0.0 `fa2F@v2.5.7-pt` is not supported because: xFormers wasn't build with CUDA support dtype=torch.float32 (supported: {torch.float16, torch.bfloat16}) `cutlassF-pt` is not supported because: xFormers wasn't build with CUDA support ``` My code shows as follows: ``` def __init__(self, params) -> None: print("begining init model ........") # self.model = SentenceTransformer(params['model_name']) self.model = LLM(model=params['model_name'], task="embedding", dtype="float32", max_model_len=int(params['max_seq_length']), trust_remote_code=True) self.params = params def generation(self, batch_data): emb_res = [] prompt_list = [] for _ in batch_data: i...

## 候选优化模式

- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: ward` with inputs: query : shape=(1, 20394, 2, 6, 128) (torch.float32) key : shape=(1, 20394, 2, 6, 128) (torch.float32) value : shape=(1, 20394, 2, 6, 128) (torch.float32) attn_bias : p : 0.0 `fa2F@v2.5.7-pt` is not su...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: NotImplementedError: No operator found for memory_efficient_attention_forward bug;stale ### Your current environment torch==2.5.1+cu124 xformers==0.0.28.post3 python==3.10 vllm==0.6.4 GPU：A100-80G ### Model Input...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: torch==2.5.1+cu124 xformers==0.0.28.post3 python==3.10 vllm==0.6.4 GPU：A100-80G ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to use **vllm==0.6.4** to accelerate **qwen2-1.5B-instruct** embedding mo...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: +cu124 xformers==0.0.28.post3 python==3.10 vllm==0.6.4 GPU：A100-80G ### Model Input Dumps _No response_ ### 🐛 Describe the bug I want to use **vllm==0.6.4** to accelerate **qwen2-1.5B-instruct** embedding model, while I...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: rt dtype=torch.float32 (supported: {torch.float16, torch.bfloat16}) `cutlassF-pt` is not supported because: xFormers wasn't build with CUDA support ``` My code shows as follows: ``` def __init__(self, params) -> None: p...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
