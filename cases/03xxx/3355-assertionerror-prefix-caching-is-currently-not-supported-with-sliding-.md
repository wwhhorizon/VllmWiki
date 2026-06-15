# vllm-project/vllm#3355: AssertionError: Prefix caching is currently not supported with sliding window attention

| 字段 | 值 |
| --- | --- |
| Issue | [#3355](https://github.com/vllm-project/vllm/issues/3355) |
| 状态 | closed |
| 标签 |  |
| 评论 | 9; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;quantization;sampling_logits |
| 子分类 | latency_reg |
| Operator 关键词 | attention;cuda;quantization |
| 症状 | crash;slowdown |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> AssertionError: Prefix caching is currently not supported with sliding window attention

### Issue 正文摘录

code ``` # 导入模块 from vllm import LLM, SamplingParams import json import os os.environ["CUDA_VISIBLE_DEVICES"] = "2" model = "/home/chenghao/workspace/OralCalculation/model/1-grade/Qwen1.5-7B-Chat-4bit/SFT_24-03-13" llm = LLM(model=model, enforce_eager=True, trust_remote_code=True, gpu_memory_utilization=0.95, dtype='auto', quantization='gptq', max_model_len=9000) # 定义数据和参数 sampling_params = SamplingParams(temperature=0.8) file = "/home/chenghao/workspace/OralCalculation/data/1-grade/OralCalculation_1_new_test.json" # for file in os.listdir(files): with open(file, 'r', encoding='utf-8') as f: datas = json.loads(f.read()) prompts = [data['system'] + '\n\n' + data['instruction'] + '\n' + data['input'] for data in datas] labels = [data['output'] for data in datas] prefix = datas[0]['system'] + '\n\n' + datas[0]['instruction'] + '\n' # -1，因为连接提示时最后一个标记可能会更改。 prefix_pos = len(llm.llm_engine.tokenizer.encode(prefix)) - 1 print(prefix_pos) # 推理 # llm.generate 调用将对所有提示进行批处理，并在资源允许的情况下立即发送批处理。 # 前缀只会在第一批处理完成后才会被缓存，因此我们需要调用一次generate来计算前缀并缓存。 outputs = llm.generate(prompts[0], sampling_params, prefix_pos=[prefix_pos]) # 后续批次可以利用缓存的前缀 outputs = llm.generate(prompts, sampling_params, prefix_po...

## 现有链接修复摘要

#3373 Fix assertion failure in Qwen 1.5 with prefix caching enabled

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: e, load_format=auto, tensor_parallel_size=1, disable_custom_all_reduce=False, quantization=gptq, enforce_eager=True, kv_cache_dtype=auto, device_config=cuda, seed=0) Special tokens have been added in the vocabulary, mak...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ngParams import json import os os.environ["CUDA_VISIBLE_DEVICES"] = "2" model = "/home/chenghao/workspace/OralCalculation/model/1-grade/Qwen1.5-7B-Chat-4bit/SFT_24-03-13" llm = LLM(model=model, enforce_eager=True, trust...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: ly not supported with sliding window attention code ``` # 导入模块 from vllm import LLM, SamplingParams import json import os os.environ["CUDA_VISIBLE_DEVICES"] = "2" model = "/home/chenghao/workspace/OralCalculation/model/...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: enforce_eager=True, trust_remote_code=True, gpu_memory_utilization=0.95, dtype='auto', quantization='gptq', max_model_len=9000) # 定义数据和参数 sampling_params = SamplingParams(temperature=0.8) file = "/home/chenghao/workspac...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: 块 from vllm import LLM, SamplingParams import json import os os.environ["CUDA_VISIBLE_DEVICES"] = "2" model = "/home/chenghao/workspace/OralCalculation/model/1-grade/Qwen1.5-7B-Chat-4bit/SFT_24-03-13" llm = LLM(model=mo...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#3373](https://github.com/vllm-project/vllm/pull/3373) | closes_keyword | 0.95 | Fix assertion failure in Qwen 1.5 with prefix caching enabled | Fix #3355. Prefix caching is currently not supported with sliding window attention, and model runner asserts `model_config.get_sliding_window()` is None. However, Qwen2/Qwen1 |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
