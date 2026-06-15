# vllm-project/vllm#11647: [Bug]: Model architectures ['Gemma2ForSequenceClassification'] are not supported for now.

| 字段 | 值 |
| --- | --- |
| Issue | [#11647](https://github.com/vllm-project/vllm/issues/11647) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Model architectures ['Gemma2ForSequenceClassification'] are not supported for now.

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know: [If your model is not in the above list, we will try to automatically convert the model using :func:vllm.model_executor.models.adapters.as_classification_model. By default, the class probabilities are extracted from the softmaxed hidden state corresponding to the last token.](https://docs.vllm.ai/en/stable/models/supported_models.html#classification-task-classify) But: ```sh ValueError: Model architectures ['Gemma2ForSequenceClassification'] are not supported for now. Supported architectures: dict_keys(['AquilaModel', .... 'MLPSpeculatorPreTrainedModel', 'Gemma2ForSeqenceClassification']) ``` **so, how to use as_classification_model ?** ```python from vllm.model_executor.models.gemma2 import Gemma2Model, Gemma2ForCausalLM from vllm.model_executor.models.adapters import as_classification_model Gemma2ForSeqenceClassification = as_classification_model(Gemma2Model) from vllm import ModelRegistry ModelRegistry.register_model("Gemma2ForSeqenceClassification", Gemma2ForSeqenceClassification) from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model="gemma2_cls"...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 10: [Bug]: Model architectures ['Gemma2ForSequenceClassification'] are not supported for now. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know: [If your model is no
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: [Bug]: Model architectures ['Gemma2ForSequenceClassification'] are not supported for now. bug ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug As far as I know: [If your model is n...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ssification_model ?** ```python from vllm.model_executor.models.gemma2 import Gemma2Model, Gemma2ForCausalLM from vllm.model_executor.models.adapters import as_classification_model Gemma2ForSeqenceClassification = as_cl...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: S"] = "0,1" llm = LLM( model="gemma2_cls", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, ) tokenizer = llm.get_tokeni...
- [KV Cache 容量、压缩与 Offload](../patterns/kv_cache_capacity_offload.md) - 分数 2: ision, tokenizer_revision, seed, gpu_memory_utilization, swap_space, cpu_offload_gb, enforce_eager, max_seq_len_to_capture, disable_custom_all_reduce, disable_async_output_proc, hf_overrides, mm_processor_kwargs, task,...

## Wiki 抽取状态

- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
