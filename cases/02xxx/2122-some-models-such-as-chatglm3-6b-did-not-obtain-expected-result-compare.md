# vllm-project/vllm#2122: Some models such as chatglm3-6b, did not obtain expected result compare to the huggingface version.

| 字段 | 值 |
| --- | --- |
| Issue | [#2122](https://github.com/vllm-project/vllm/issues/2122) |
| 状态 | closed |
| 标签 |  |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;quantization;sampling_logits |
| 子分类 | memory |
| Operator 关键词 | cuda;quantization;sampling |
| 症状 |  |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> Some models such as chatglm3-6b, did not obtain expected result compare to the huggingface version.

### Issue 正文摘录

Hi team, I tested chatglm3-6b with vLLM but obtained poor results because the tokenizer did not perform as model expect. 1. first i test huggingface model.chat function. ```python from transformers import AutoModel, AutoConfig, AutoTokenizer from torch import cuda, bfloat16 import transformers model_id = '/data/models/ZhipuAI/chatglm3-6b' device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'cpu' # set quantization configuration to load large model with less GPU memory # this requires the `bitsandbytes` library bnb_config = transformers.BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_quant_type='nf4', bnb_4bit_use_double_quant=True, bnb_4bit_compute_dtype=bfloat16 ) # begin initializing HF items, need auth token for these tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True) model_config = transformers.AutoConfig.from_pretrained(model_id, trust_remote_code=True) model = AutoModel.from_pretrained(model_id, trust_remote_code=True, config=model_config, quantization_config=bnb_config, device_map={"": device}) model.eval() print(f"load model to {device}") his = [] res, his = model.chat(tokenizer, "你是谁？", history=his) print(res) ``` obtain the good...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: s chatglm3-6b, did not obtain expected result compare to the huggingface version. Hi team, I tested chatglm3-6b with vLLM but obtained poor results because the tokenizer did not perform as model expect. 1. first i test...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: mers import AutoModel, AutoConfig, AutoTokenizer from torch import cuda, bfloat16 import transformers model_id = '/data/models/ZhipuAI/chatglm3-6b' device = f'cuda:{cuda.current_device()}' if cuda.is_available() else 'c...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: Some models such as chatglm3-6b, did not obtain expected result compare to the huggingface version. Hi team, I tested chatglm3-6b with vLLM but obtained poor results because the tokenizer did not perform as model expect...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ansformers import AutoModel, AutoConfig, AutoTokenizer from torch import cuda, bfloat16 import transformers model_id = '/data/models/ZhipuAI/chatglm3-6b' device = f'cuda:{cuda.current_device()}' if cuda.is_available() e...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 2: t obtain expected result compare to the huggingface version. Hi team, I tested chatglm3-6b with vLLM but obtained poor results because the tokenizer did not perform as model expect. 1. first i test huggingface model.cha...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
