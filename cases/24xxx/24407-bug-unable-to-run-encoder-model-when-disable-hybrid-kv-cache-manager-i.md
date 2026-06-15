# vllm-project/vllm#24407: [Bug]: Unable to run encoder model when disable_hybrid_kv_cache_manager is true

| 字段 | 值 |
| --- | --- |
| Issue | [#24407](https://github.com/vllm-project/vllm/issues/24407) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | activation_norm;attention_kv_cache;ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;moe;quantization;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | attention;cuda;operator;quantization;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Unable to run encoder model when disable_hybrid_kv_cache_manager is true

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python from argparse import Namespace from vllm import LLM, EngineArgs from vllm.utils import FlexibleArgumentParser def parse_args(): parser = FlexibleArgumentParser() parser = EngineArgs.add_cli_args(parser) # Set example specific arguments parser.set_defaults( model="/weight/bge/BAAI_bge-reranker-v2-m3/", task="score", enforce_eager=True, disable_hybrid_kv_cache_manager=True ) return parser.parse_args() def main(args: Namespace): # Sample prompts. text_1 = "What is your favourite fruit?" texts_2 = [ "Banana.", "Apple.", ] # Create an LLM. # You should pass task="score" for cross-encoder models llm = LLM(**vars(args)) # Generate scores. The output is a list of ScoringRequestOutputs. outputs = llm.score(text_1, texts_2) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for text_2, output in zip(texts_2, outputs): score = output.outputs.score print(f"Pair: {[text_1, text_2]!r} \nScore: {score}") print("-" * 60) if __name__ == "__main__": args = parse_args() main(args) ``` ### Traceback ```text INFO 09-07 19:28:24 [__init__.py:241] Automatically detected platform cuda. INFO 09-07 19:28:25 [utils.py:328] non-defaul...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 6: current environment ### 🐛 Describe the bug ```python from argparse import Namespace from vllm import LLM, EngineArgs from vllm.utils import FlexibleArgumentParser def parse_args(): parser = FlexibleArgumentParser() pars...
- [Backend 路由与 Fallback](../patterns/backend_routing_fallback.md) - 分数 5: kv_cache_dtype=auto, device_config=cuda, decoding_config=DecodingConfig(backend='auto', disable_fallback=False, disable_any_whitespace=False, disable_additional_properties=False, reasoning_backend=''), observability_con...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 4: eClassification INFO 09-07 19:28:29 [__init__.py:2881] Downcasting torch.float32 to torch.float16. INFO 09-07 19:28:29 [__init__.py:1773] Using max model len 8192 INFO 09-07 19:28:29 [arg_utils.py:1624] (Disabling) chun...
- [MoE、GEMM 与 Expert Routing](../patterns/moe_gemm_routing.md) - 分数 4: :28:25 [utils.py:328] non-default args: {'task': 'score', 'num_redundant_experts': None, 'eplb_window_size': None, 'eplb_step_interval': None, 'eplb_log_balancedness': None, 'enforce_eager': True, 'enable_lora': None, '...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 4: LLM(**vars(args)) # Generate scores. The output is a list of ScoringRequestOutputs. outputs = llm.score(text_1, texts_2) # Print the outputs. print("\nGenerated Outputs:\n" + "-" * 60) for text_2, output in zip(texts_2,...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
