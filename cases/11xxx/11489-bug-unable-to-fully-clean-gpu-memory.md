# vllm-project/vllm#11489: [Bug]: Unable to fully clean GPU memory

| 字段 | 值 |
| --- | --- |
| Issue | [#11489](https://github.com/vllm-project/vllm/issues/11489) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;kernel;sampling;triton |
| 症状 | build_error |
| 根因提示 | env_dependency;race_condition |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to fully clean GPU memory

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we run the following code on a machine with a single GPU and two cards, we cannot completely clear the cache on Card 0 and there will always be about 1 GB of remaining cache. Graphics card model: 2 x GeForce RTX 4090 with 24GB of memory. ```python class VLLM_Qwen_Chat(LLM): model_name_or_path = "/data/model/Qwen2.5-7B-Instruct" tokenizer: AutoTokenizer = None sampling_params: vllm.SamplingParams = None llm: vllm.LLM = None history: list = [] MAX_HISTORY_LEN: int = 5 tensor_parallel_size = 2 gpu_memory_utilization = 0.98 def __init__(self): super(VLLM_Qwen_Chat, self).__init__() self.tokenizer = AutoTokenizer.from_pretrained( self.model_name_or_path, use_fast=False, trust_remote_code=True ) self.sampling_params = vllm.SamplingParams( temperature=0.01, top_p=0.8, repetition_penalty=1.05, max_tokens=1024 ) self.llm = vllm.LLM( model=self.model_name_or_path, tensor_parallel_size=self.tensor_parallel_size, gpu_memory_utilization=self.gpu_memory_utilization ) logger.info("完成本地模型的加载") def _call(self, prompt: str, **kwargs: Any): messages = [ {"role": "user", "content": prompt} ] text = self.token...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 4: ways be about 1 GB of remaining cache. Graphics card model: 2 x GeForce RTX 4090 with 24GB of memory. ```python class VLLM_Qwen_Chat(LLM): model_name_or_path = "/data/model/Qwen2.5-7B-Instruct" tokenizer: AutoTokenizer...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: nswer lots of frequently asked questions. performance attention_kv_cache;ci_build;distributed_parallel;frontend_api;model_support;sampling_logits cuda;kernel;sampling;triton build_error env_dependency;race_condition You...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: to fully clean GPU memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we run the following code on a machine with a single GPU and two cards, we cannot complete...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: parallel;frontend_api;model_support;sampling_logits cuda;kernel;sampling;triton build_error env_dependency;race_condition Your current environment
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 1: [Bug]: Unable to fully clean GPU memory bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When we run the following code on a machine with a single GPU and two cards, we c...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
