# vllm-project/vllm#536: OOM due to long context length with MPT-7B

| 字段 | 值 |
| --- | --- |
| Issue | [#536](https://github.com/vllm-project/vllm/issues/536) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | performance |
| 工作域 | attention_kv_cache;frontend_api;model_support;sampling_logits;scheduler_memory |
| 子分类 | memory |
| Operator 关键词 | attention;cuda;sampling |
| 症状 | oom |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> OOM due to long context length with MPT-7B

### Issue 正文摘录

I'm running into OOM while trying to run MPT-7B on a context length of >20K on 8 H100 80GB GPUs. It seems that MPT-Storywriter, which goes up to 65K context, is supported so I'm wondering if there is something wrong with the way I'm implementing this: I use a version of the MPT-7B that was been finetuned on some internal data, referenced in `model_path`. ``` llm = LLM(model=model_path, max_num_batched_tokens=20000, block_size=32, gpu_memory_utilization=0.95, tensor_parallel_size=8, ) ``` This initializes the model as ``` INFO 07-20 19:23:49 llm_engine.py:60] Initializing an LLM engine with config: model='/root/MPT-exps/MHS2.2.3_finetune/medmpt_coding2.2.3_ep4/', tokenizer='/root/MPT-exps/MHS2.2.3_finetune/medmpt_coding2.2.3_ep4/', tokenizer_mode=auto, dtype=torch.bfloat16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=8, seed=0) INFO 07-20 19:27:06 llm_engine.py:131] # GPU blocks: 37085, # CPU blocks: 2048 ``` Then, running the following gives me an OOM: ``` sampling_params = SamplingParams(n=1, temperature=0.95, top_p=0.9, best_of=1, use_beam_search=False, stop=" ", max_tokens=500, ) outputs = llm.generate(example_text, sampling_params) ``...

## 候选优化模式

- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 4: LLM(model=model_path, max_num_batched_tokens=20000, block_size=32, gpu_memory_utilization=0.95, tensor_parallel_size=8, ) ``` This initializes the model as ``` INFO 07-20 19:23:49 llm_engine.py:60] Initializing an LLM e...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: if there is something wrong with the way I'm implementing this: I use a version of the MPT-7B that was been finetuned on some internal data, referenced in `model_path`. ``` llm = LLM(model=model_path, max_num_batched_to...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: PT-exps/MHS2.2.3_finetune/medmpt_coding2.2.3_ep4/', tokenizer_mode=auto, dtype=torch.bfloat16, use_dummy_weights=False, download_dir=None, use_np_weights=False, tensor_parallel_size=8, seed=0) INFO 07-20 19:27:06 llm_en...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: ing into OOM while trying to run MPT-7B on a context length of >20K on 8 H100 80GB GPUs. It seems that MPT-Storywriter, which goes up to 65K context, is supported so I'm wondering if there is something wrong with the wa...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: the MPT-7B that was been finetuned on some internal data, referenced in `model_path`. ``` llm = LLM(model=model_path, max_num_batched_tokens=20000, block_size=32, gpu_memory_utilization=0.95, tensor_parallel_size=8, ) `...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
