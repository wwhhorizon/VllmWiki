# vllm-project/vllm#11802: [Bug]:  Some weights are not initialized from checkpoints For Gemma2ForSequenceClassification

| 字段 | 值 |
| --- | --- |
| Issue | [#11802](https://github.com/vllm-project/vllm/issues/11802) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 26; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:  Some weights are not initialized from checkpoints For Gemma2ForSequenceClassification

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model_executor.models.gemma2 import Gemma2Model, Gemma2ForCausalLM from vllm.model_executor.models.adapters import as_classification_model Gemma2ForSequenceClassification = as_classification_model(Gemma2ForCausalLM) from vllm import ModelRegistry ModelRegistry.register_model("Gemma2ForSequenceClassification", Gemma2ForSequenceClassification) from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model="gemma2-cls", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, ) ``` ```python WARNING 01-07 07:39:33 gemma2.py:372] Some weights are not initialized from checkpoints: {'layers.23.mlp.down_proj.weight', 'layers.23.post_attention_layernorm.weight', 'layers.3.mlp.gate_up_proj.weight', 'layers.16.self_attn.o_proj.weight', 'layers.27.mlp.down_proj.weight', 'layers.7.post_attention_layernorm.weight', 'layers.32.mlp.down_proj.weight', 'layers.9.input_layernorm.weight', 'layers.26.pre_feedforward_layernorm.weight', 'layers.31.mlp.gate_up_proj.weight', 'layers.32.post_...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ion", Gemma2ForSequenceClassification) from vllm import LLM os.environ["CUDA_VISIBLE_DEVICES"] = "0,1" llm = LLM( model="gemma2-cls", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, t...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: [Bug]: Some weights are not initialized from checkpoints For Gemma2ForSequenceClassification bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model_ex...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ## 🐛 Describe the bug ```python from vllm.model_executor.models.gemma2 import Gemma2Model, Gemma2ForCausalLM from vllm.model_executor.models.adapters import as_classification_model Gemma2ForSequenceClassification = as_c...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: S"] = "0,1" llm = LLM( model="gemma2-cls", task="classify", dtype="half", tensor_parallel_size=2, gpu_memory_utilization=0.98, trust_remote_code=True, max_model_len=1024, enforce_eager=True, ) ``` ```python WARNING 01-0...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 1: [Bug]: Some weights are not initialized from checkpoints For Gemma2ForSequenceClassification bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug ```python from vllm.model_ex...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
