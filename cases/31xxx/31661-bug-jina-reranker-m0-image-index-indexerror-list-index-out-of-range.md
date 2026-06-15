# vllm-project/vllm#31661: [Bug]: jina-reranker-m0 [image_index]   IndexError: list index out of range

| 字段 | 值 |
| --- | --- |
| Issue | [#31661](https://github.com/vllm-project/vllm/issues/31661) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 4; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | development |
| 工作域 | ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory |
| 子分类 | env_compat |
| Operator 关键词 | cuda;operator;triton |
| 症状 | build_error;crash |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: jina-reranker-m0 [image_index]   IndexError: list index out of range

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug 部署 jina-reranker-m0 报错 t, h, w = image_grid_thw[image_index] self.model = LLM( model=self.config['model_path'], runner="pooling", tensor_parallel_size=self.number_of_gpu, trust_remote_code=True, max_model_len=16384, enable_prefix_caching=False, limit_mm_per_prompt={"image": 0}, mm_processor_kwargs={ "max_pixels": 602112, "min_pixels": 3136, }, gpu_memory_utilization=0.8, max_num_seqs=16, enforce_eager=True, disable_log_stats=False, ) [0;36m(EngineCore_DP0 pid=33410)[0;0m ERROR 12-30 20:24:29 [dump_input.py:79] Dumping scheduler output for model execution: SchedulerOutput(scheduled_new_reqs=[NewRequestData(req_id=21875,prompt_token_ids_len=802,mm_features=[],sampling_params=None,block_ids=([11455, 11501, 11500, 11466, 11465, 11464, 11463, 11480, 11479, 11478, 11477, 11476, 11525, 11524, 11498, 11497, 11444, 11443, 11442, 11473, 11472, 11471, 11504, 11593, 11592, 11591, 11590, 11589, 11588, 11587, 11459, 11561, 11560, 11559, 11558, 11499, 11515, 11514, 11513, 11512, 11511, 11454, 11493, 11492, 11491, 11490, 11489, 11523, 11462, 11461, 11460],),num_computed_tokens=0,lora_request=None,prompt_embeds_shape=None), NewRequestData(req_id...

## 现有链接修复摘要

#39695 Introduce De-dup/Similarity-Check in CI Workflow for PR/Issue

## 候选优化模式

- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: jina-reranker-m0 [image_index] IndexError: list index out of range bug;stale ### Your current environment ### 🐛 Describe the bug 部署 jina-reranker-m0 报错 t, h, w = image_grid_thw[image_index] self.model = LLM( model=self....
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 3: test/), which can answer lots of frequently asked questions. development ci_build;distributed_parallel;frontend_api;gemm_linear;hardware_porting;model_support;scheduler_memory cuda;operator;triton build_error;crash env_...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: _code=True, max_model_len=16384, enable_prefix_caching=False, limit_mm_per_prompt={"image": 0}, mm_processor_kwargs={ "max_pixels": 602112, "min_pixels": 3136, }, gpu_memory_utilization=0.8, max_num_seqs=16,
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 部署 jina-reranker-m0 报错 t, h, w = image_grid_thw[image_index] self.model = LLM( model=self.config['model_path'], runner="pooling", tensor_parallel_size=self.number_of_gpu, trust_remote_code=True, max_model_len=16384, ena...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: nge ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## 关联 PR 证据

| PR | 链接类型 | 置信度 | PR 标题 | 证据 |
| --- | --- | ---: | --- | --- |
| [#39695](https://github.com/vllm-project/vllm/pull/39695) | mentioned | 0.6 | Introduce De-dup/Similarity-Check in  CI Workflow for PR/Issue | ers v5] NemotronParseForConditionalGeneration \| \| 76% \| 88% \| 31% \| [#31661](https://github.com/vllm-project/vllm/issues/31661) [Bug]: jina-reranker-m0 [image_index] IndexError: l… |

## Wiki 抽取状态

- 后续迭代应在可用时读取完整讨论评论。
