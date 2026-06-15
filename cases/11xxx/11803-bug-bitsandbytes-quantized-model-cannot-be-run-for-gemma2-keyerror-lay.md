# vllm-project/vllm#11803: [Bug]: bitsandbytes quantized model cannot be run for Gemma2:  KeyError: 'layers.30.mlp.down_proj.SCB'

| 字段 | 值 |
| --- | --- |
| Issue | [#11803](https://github.com/vllm-project/vllm/issues/11803) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: bitsandbytes quantized model cannot be run for Gemma2:  KeyError: 'layers.30.mlp.down_proj.SCB'

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model_executor.models.gemma2 import Gemma2Model, Gemma2ForCausalLM from vllm.model_executor.models.adapters import as_classification_model Gemma2ForSequenceClassification = as_classification_model(Gemma2ForCausalLM) from vllm import ModelRegistry ModelRegistry.register_model("Gemma2ForSequenceClassification", Gemma2ForSequenceClassification) from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0" llm = LLM( model="gemma2-cls-bnb-8bit", task="classify", dtype="half", tensor_parallel_size=1, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, ) ``` ```python --------------------------------------------------------------------------- KeyError Traceback (most recent call last) in () 14 WEIGHTS_PATH = "/kaggle/input/distill-gemma2-fold0" 15 MAX_LENGTH = 3072 ---> 16 llm = LLM( 17 model=MODEL_NAME, 18 task="classify", /usr/local/lib/python3.10/dist-packages/vllm/utils.py in inner(*args, **kwargs) 984 ) 985 --> 986 return fn(*args, **kwargs) 987 988 return inner # type: ignore /usr/local/lib/python3.10/dist-packages/vllm/entrypoints/ll...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: [Bug]: bitsandbytes quantized model cannot be run for Gemma2: KeyError: 'layers.30.mlp.down_proj.SCB' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: [Bug]: bitsandbytes quantized model cannot be run for Gemma2: KeyError: 'layers.30.mlp.down_proj.SCB' bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion", Gemma2ForSequenceClassification) from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0" llm = LLM( model="gemma2-cls-bnb-8bit", task="classify", dtype="half", tensor_parallel_size=1, gpu_memory_utilization=...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: model %s...", self.model_config.model) 1095 with DeviceMemoryProfiler() as m: -> 1096 self.model = get_model(vllm_config=self.vllm_config) 1097 1098 self.model_memory_usage = m.consumed_memory /usr/local/lib/python3.10/...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: ig_cls.load_weights(self, weights) # type: ignore 106 # Fallback 107 else: /usr/local/lib/python3.10/dist-packages/vllm/model_executor/models/gemma2.py in load_weights(self, weights) 469 if self.config.tie_word_embeddin...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
