# vllm-project/vllm#792: InternLM-Chat-7B's outputs can't stop properly after SFT under vLLM

| 字段 | 值 |
| --- | --- |
| Issue | [#792](https://github.com/vllm-project/vllm/issues/792) |
| 状态 | closed |
| 标签 |  |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;sampling |
| 症状 | mismatch |
| 根因提示 | env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> InternLM-Chat-7B's outputs can't stop properly after SFT under vLLM

### Issue 正文摘录

I trained a model based on InternLM-Chat-7B, nothing changed except the vocabulary, I modified the special tokens of it. I run the following code with transformers package, and it's outputs are normal: ```python _tokenizer = AutoTokenizer.from_pretrained(sum_model_path, trust_remote_code=True) _model = AutoModelForCausalLM.from_pretrained(sum_model_path, trust_remote_code=True, torch_dtype=torch.float16, device_map='cpu') _device = torch.device('cuda:5') _model.to(_device) input = "Who are you?" _response, _ = _model.chat(_tokenizer, input, history=[], max_new_tokens=512, do_sample=False) ``` According to the logs, it met the eos_token_id `103169` and stopped. ```shell prompt: Who are you? input_ids: [1, 103173, 15315, 657, 629, 345, 103170, 103168] eos_token_ids: [2, 103173, 103168, 103174, 103171, 103172, 103170, 103169] outputs: [295, 1221, 589, 15358, 4287, 1762, 328, 489, 1658, 1082, 746, 395, 963, 607, 395, 17435, 281, 489, 1221, 54039, 442, 3572, 11100, 454, 38061, 14644, 442, 829, 43469, 281, 103169] response: I am a computer program that is designed to help people with their writing tasks. I can assist with grammar, spelling, and style checks, as well as provide suggestio...

## 候选优化模式

- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ue, torch_dtype=torch.float16, device_map='cpu') _device = torch.device('cuda:5') _model.to(_device) input = "Who are you?" _response, _ = _model.chat(_tokenizer, input, history=[], max_new_tokens=512, do_sample=False)...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: ternLM-Chat-7B, nothing changed except the vocabulary, I modified the special tokens of it. I run the following code with transformers package, and it's outputs are normal: ```python _tokenizer = AutoTokenizer.from_pret...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 2: orCausalLM.from_pretrained(sum_model_path, trust_remote_code=True, torch_dtype=torch.float16, device_map='cpu') _device = torch.device('cuda:5') _model.to(_device) input = "Who are you?" _response, _ = _model.chat(_toke...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ng? correctness frontend_api;model_support;sampling_logits cuda;sampling mismatch env_dependency I trained a model based on InternLM-Chat-7B, nothing changed except the vocabulary, I modified the special tokens of it.
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: odel.chat(_tokenizer, input, history=[], max_new_tokens=512, do_sample=False) ``` According to the logs, it met the eos_token_id `103169` and stopped. ```shell prompt: Who are you? input_ids: [1, 103173, 15315, 657, 629...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
