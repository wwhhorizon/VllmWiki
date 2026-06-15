# vllm-project/vllm#14394: [Bug]: vllm-0.7.3. gptq-int3 model cannot run.

| 字段 | 值 |
| --- | --- |
| Issue | [#14394](https://github.com/vllm-project/vllm/issues/14394) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: vllm-0.7.3. gptq-int3 model cannot run.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug infer code: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name = "Xu-Ouyang/Qwen2-1.5B-int3-GPTQ-wikitext2" max_model_len, tp_size = 1024, 1 tokenizer = AutoTokenizer.from_pretrained(model_name) llm = LLM(model=model_name, tensor_parallel_size=tp_size, max_model_len=max_model_len, trust_remote_code=True, enforce_eager=True) sampling_params = SamplingParams(temperature=0.3, max_tokens=128, stop_token_ids=[tokenizer.eos_token_id]) messages_list = [[{"role": "user", "content": "Who are you?"}],] prompt_token_ids = [tokenizer.apply_chat_template(messages, add_generation_prompt=True) for messages in messages_list] outputs = llm.generate(prompt_token_ids=prompt_token_ids, sampling_params=sampling_params) generated_text = [output.outputs[0].text for output in outputs] print(generated_text) ``` error: ```text [rank0]: File "/media/zjin/Data/projects/tst/vllm/vllm/model_executor/layers/linear.py", line 336, in __init__ [rank0]: self.quant_method.create_weights( [rank0]: File "/media/zjin/Data/projects/tst/vllm/vllm/model_executor/layers/quantization/gptq.py", line 153, in create_weights [rank0...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Bug]: vllm-0.7.3. gptq-int3 model cannot run. bug;stale ### Your current environment ### 🐛 Describe the bug infer code: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name =...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ment ### 🐛 Describe the bug infer code: ```python from transformers import AutoTokenizer from vllm import LLM, SamplingParams model_name = "Xu-Ouyang/Qwen2-1.5B-int3-GPTQ-wikitext2" max_model_len, tp_size = 1024, 1 toke...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: odel_executor/layers/linear.py", line 336, in __init__ [rank0]: self.quant_method.create_weights( [rank0]: File "/media/zjin/Data/projects/tst/vllm/vllm/model_executor/layers/quantization/gptq.py", line 153, in create_w...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: this process. In rare cases this process can exit before this point and block the progress of another member of the process group. This constraint has always been present, but this warning has only been added since PyTo...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
