# vllm-project/vllm#216: vLLM is 4x faster than HF for offline inference

| 字段 | 值 |
| --- | --- |
| Issue | [#216](https://github.com/vllm-project/vllm/issues/216) |
| 状态 | closed |
| 标签 |  |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | frontend_api;model_support;sampling_logits |
| 子分类 |  |
| Operator 关键词 | sampling |
| 症状 |  |
| 根因提示 |  |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> vLLM is 4x faster than HF for offline inference

### Issue 正文摘录

Thanks for the great project. I gave a try and compared with hf's offline inference speed on 100 alpaca examples. The hardware I used is a single v100-40G GPU. Here is my script for vLLM: ``` sampling_params = SamplingParams(temperature=0.1, top_p=0.75, top_k=40, max_tokens=128, ignore_eos=True) llm = LLM(model="openlm-research/open_llama_13b") # Prepare dataset. start_time = time.time() for data in my_dataset: # Set ignore_eos to True so it generates max_tokens. llm.generate(data, sampling_params, ignore_eos=True) end_time = time.time() ``` and for hf: ``` model = LlamaForCausalLM.from_pretrained("openlm-research/open_llama_7b") tokenizer = ... generation_config = GenerationConfig(temperature=temperature, top_p=top_p, top_k=top_k, ...) # Prepare dataset. start_time = time.time() for data in my_dataset: input_ids = tokenizer(data)["input_ids"] model.generate(input_ids, generation_config, max_new_tokens=128) end_time = time.time() ``` | API | Model Size | Time (minutes) | | --- | ----------- |---| | HF | 7B | 12.7 | | vLLM | 7B | 3.1 | | HF | 13B | 15.8 | | vLLM | 13B | 5.3 | It seems that the speedup is ~3-4x (not 25x). Am I missing a special setup for vLLM? Thanks.

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: vLLM is 4x faster than HF for offline inference Thanks for the great project. I gave a try and compared with hf's offline inference speed on 100 alpaca examples. The hardware I used is a single v100-40G GPU. Here is my...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: | 5.3 | It seems that the speedup is ~3-4x (not 25x). Am I missing a special setup for vLLM? Thanks. performance frontend_api;model_support;sampling_logits sampling Thanks for the great project.
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: , top_k=40, max_tokens=128, ignore_eos=True) llm = LLM(model="openlm-research/open_llama_13b") # Prepare dataset. start_time = time.time() for data in my_dataset: # Set ignore_eos to True so it generates max_tokens. llm...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
