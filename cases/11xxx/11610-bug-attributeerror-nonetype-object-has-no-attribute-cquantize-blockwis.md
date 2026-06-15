# vllm-project/vllm#11610: [Bug]: AttributeError: 'NoneType' object has no attribute 'cquantize_blockwise_fp16_nf4'

| 字段 | 值 |
| --- | --- |
| Issue | [#11610](https://github.com/vllm-project/vllm/issues/11610) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 1; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: AttributeError: 'NoneType' object has no attribute 'cquantize_blockwise_fp16_nf4'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use a custom `Qwen2ForSequenceClassification` with **vllm-0.6.3** (and **bitsandbytes==0.44.1**), it works perfectly. However, when I switch to **vllm-0.6.6** (and **bitsandbytes==0.45.0**), I encounter the error: `AttributeError: 'NoneType' object has no attribute 'cquantize_blockwise_fp16_nf4'`. It seems that the issue is caused by **bitsandbytes >= 0.45.0**??? ```python from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model="qwen2.5-14b", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, quantization="bitsandbytes", load_format="bitsandbytes", ) ``` ```sh AttributeError Traceback (most recent call last) in () 2 os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" 3 ----> 4 llm = LLM( 5 model=MODEL_NAME, 6 task="classify", /usr/local/lib/python3.10/dist-packages/vllm/utils.py in inner(*args, **kwargs) 988 ) 989 --> 990 return fn(*args, **kwargs) 991 992 return inner # type: ignore /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/llm.py in __init__(self, model, token...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: 'cquantize_blockwise_fp16_nf4' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use a custom `Qwen2ForSequenceClassification` with **vllm-0.6.3** (and **bitsandbytes==0....
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: [Bug]: AttributeError: 'NoneType' object has no attribute 'cquantize_blockwise_fp16_nf4' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use a custom `Qwen2ForSequenceC...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: *bitsandbytes >= 0.45.0**??? ```python from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model="qwen2.5-14b", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98,...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 3: model %s...", self.model_config.model) 1093 with DeviceMemoryProfiler() as m: -> 1094 self.model = get_model(vllm_config=self.vllm_config) 1095 1096 self.model_memory_usage = m.consumed_memory /usr/local/lib/python3.10/...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 2: [Bug]: AttributeError: 'NoneType' object has no attribute 'cquantize_blockwise_fp16_nf4' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug When I use a custom `Qwen2ForSequenceC...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
