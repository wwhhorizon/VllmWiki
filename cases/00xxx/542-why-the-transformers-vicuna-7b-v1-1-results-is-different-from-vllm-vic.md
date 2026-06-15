# vllm-project/vllm#542: why  the transformers vicuna-7b-v1.1 results is different from vllm vicuna-7b-v1.1 results,   How to solve it，thanks

| 字段 | 值 |
| --- | --- |
| Issue | [#542](https://github.com/vllm-project/vllm/issues/542) |
| 状态 | closed |
| 标签 |  |
| 评论 | 3; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> why  the transformers vicuna-7b-v1.1 results is different from vllm vicuna-7b-v1.1 results,   How to solve it，thanks

### Issue 正文摘录

transformers vicuna-7b-v1.1 script: ``` from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-7b-v1.1") model = AutoModelForCausalLM.from_pretrained("lmsys/vicuna-7b-v1.1").to(0) import time prompts = [ "Hello, my name is", "The president of the United States is", "The capital of France is", "The future of AI is", ] for prompt in prompts: inputs = tokenizer(prompt, return_tensors="pt").to(0) generate_ids = model.generate(inputs.input_ids, max_length=256) result = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] print(result) ``` the results is: ``` Hello, my name is Dr. David C. Preston, and I am a chiropractor serving the residents of the greater Phoenix area. I have been in practice for over 20 years, and I am dedicated to helping my patients achieve optimal health and wellness through natural, non-invasive chiropractic care. At my practice, I offer a wide range of chiropractic services, including adjustments, massage therapy, and rehabilitation. I also offer nutritional counseling and weight loss coaching to help my patients achieve their health goals. I believe t...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: olve it，thanks transformers vicuna-7b-v1.1 script: ``` from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-7b-v1.1") model = AutoModelForCausalLM.from_pre...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: p his sexual misconduct. He is a man who has been accused of sexual harassment by at least one woman, and who has been accused of using his position of power to force himself on women. He is a man who has been accused o...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: e(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] print(result) ``` the results is: ``` Hello, my name is Dr. David C. Preston, and I am a chiropractor serving the residents of the greater...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: s vicuna-7b-v1.1 script: ``` from transformers import AutoTokenizer, AutoModelForCausalLM tokenizer = AutoTokenizer.from_pretrained("lmsys/vicuna-7b-v1.1") model = AutoModelForCausalLM.from_pretrained("lmsys/vicuna-7b-v...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: .generate(inputs.input_ids, max_length=256) result = tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0] print(result) ``` the results is: ``` Hello, my name is Dr. Davi...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
