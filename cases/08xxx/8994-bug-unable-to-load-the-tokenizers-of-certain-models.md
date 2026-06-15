# vllm-project/vllm#8994: [Bug]: Unable to load the tokenizers of certain models

| 字段 | 值 |
| --- | --- |
| Issue | [#8994](https://github.com/vllm-project/vllm/issues/8994) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 11; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf;slowdown |
| 根因提示 | env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to load the tokenizers of certain models

### Issue 正文摘录

### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to load llama-2-13B and alma-13B models and I am gettign errors related to the tokenizers. note that loading the 7B version of the models works fine. vllm and transformers versions that I am using are shown in the environment details. Here is the log of the errors: ## llama-2-13B ``` model = LLM(model=name_path,seed=42,trust_remote_code=True,tensor_parallel_size=1) File "/home/wmohammed/.conda/envs/alti/lib/python3.10/site-packages/vllm/entrypoints/llm.py", line 214, in __init__ self.llm_engine = LLMEngine.from_engine_args( File "/home/wmohammed/.conda/envs/alti/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 574, in from_engine_args engine = cls( File "/home/wmohammed/.conda/envs/alti/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 309, in __init__ self.tokenizer = self._init_tokenizer() File "/home/wmohammed/.conda/envs/alti/lib/python3.10/site-packages/vllm/engine/llm_engine.py", line 618, in _init_tokenizer return init_tokenizer_from_configs( File "/home/wmohammed/.conda/envs/alti/lib/python3.10/site-packages/vllm/transformers_utils/tokenizer_group/__...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 5: [Bug]: Unable to load the tokenizers of certain models bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to load llama-2-13B and alma-13B models and I am getti...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: I am gettign errors related to the tokenizers. note that loading the 7B version of the models works fine. vllm and transformers versions that I am using are shown in the environment details. Here is the log of the error...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 3: , 'RetriBertTokenizer', 'RobertaTokenizer', 'RoFormerTokenizer', 'SeamlessM4TTokenizer', 'SqueezeBertTokenizer', 'T5Tokenizer', 'UdopTokenizer', 'WhisperTokenizer', 'XLMRobertaTokenizer', 'XLNetTokenizer', 'SplinterToke...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: [Bug]: Unable to load the tokenizers of certain models bug;stale ### Your current environment ### Model Input Dumps _No response_ ### 🐛 Describe the bug I am trying to load llama-2-13B and alma-13B models and I am getti...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 1: odel_support;sampling_logits;speculative_decoding cuda;operator;sampling;triton build_error;crash;nan_inf;slowdown env_dependency Your current environment

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
