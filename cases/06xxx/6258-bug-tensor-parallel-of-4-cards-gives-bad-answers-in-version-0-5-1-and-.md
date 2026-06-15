# vllm-project/vllm#6258: [Bug]: tensor parallel (of 4 cards) gives bad answers in version 0.5.1 and later (compared to 0.4.1) with gptq marlin kernels (compared to gptq)

| 字段 | 值 |
| --- | --- |
| Issue | [#6258](https://github.com/vllm-project/vllm/issues/6258) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: tensor parallel (of 4 cards) gives bad answers in version 0.5.1 and later (compared to 0.4.1) with gptq marlin kernels (compared to gptq)

### Issue 正文摘录

### Your current environment sagemaker ml.g5.12xlarge instance (4 instances of a10g 24gb) container is 763104351884.dkr.ecr.us-west-2.amazonaws.com/djl-inference:0.27.0-deepspeed0.12.6-cu121 from https://github.com/aws/deep-learning-containers/blob/master/available_images.md ### 🐛 Describe the bug from vllm import LLM, SamplingParams question = "what is the id of the team and what is the subtitute lineup of the home team for the match?" history = str(["how many games the home team Sevilla won?"]) full_example = f""" \n \n\nYou are a transformation helper specialist, based on the history helping in transforming user input\nto a more structured and simpler text to a smaller model, which is less smart as you. \n\nMost of the times, the history could help you about entities which are now missing \nfrom the question\nTo illustrate the mission, if the user asked in the history about an entity (like \'Barcelona\'), and \nnow he asked about \'team\' (could be team, player, or other entity) or it seems to you that the an entity \nis missing in the context, perhaps the entity (\'Barcelona\') from the history could be the option to fill the gap. \n\nIf there is no entity in the history, plea...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: [Bug]: tensor parallel (of 4 cards) gives bad answers in version 0.5.1 and later (compared to 0.4.1) with gptq marlin kernels (compared to gptq) bug ### Your current environment sagemaker ml.g5.12xlarge instance (4 inst...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: me team Sevilla won?"]) full_example = f""" \n \n\nYou are a transformation helper specialist, based on the history helping in transforming user input\nto a more structured and simpler text to a smaller model, which is...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: 'tokenizer_mode'='auto', 'gpu_memory_utilization'=0.7, 'guided_decoding_backend' ='lm-format-enforcer', tensor_parallel_size=4) quantization not mentioned in order to get marlin kernels instead of standard gptq (if avai...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: guided_decoding_backend' ='lm-format-enforcer', tensor_parallel_size=4) quantization not mentioned in order to get marlin kernels instead of standard gptq (if available). outputs = llm.generate(prompts, sampling_params)...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: g in transforming user input\nto a more structured and simpler text to a smaller model, which is less smart as you. \n\nMost of the times, the history could help you about entities which are now missing \nfrom the quest...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
