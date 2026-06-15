# vllm-project/vllm#8664: [Usage]: how to let vllm use the generation_config.json as the default generation config

| 字段 | 值 |
| --- | --- |
| Issue | [#8664](https://github.com/vllm-project/vllm/issues/8664) |
| 状态 | closed |
| 标签 | usage |
| 评论 | 2; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Usage]: how to let vllm use the generation_config.json as the default generation config

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` vLLM Version: 0.6.1.post2@9ba0817ff1eb514f51cc6de9cb8e16c98d6ee44f model: Qwen2-VL-7B-Instruct ### How would you like to use vllm My starting cmd `python -m vllm.entrypoints.openai.api_server --served-model-name Qwen2-VL-7B-Instruct --model /data/modelscope_cache/Qwen/Qwen2-VL-7B-Instruct` The log is showing ![image](https://github.com/user-attachments/assets/339f2e3d-15e7-41ae-91f4-f171000ed481) These configs are not the same as ones in the generation_config.json. Two questions: 1. Does vllm use the generation_config.json as the default generation config? 2. If not, how to set?

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: [Usage]: how to let vllm use the generation_config.json as the default generation config usage ### Your current environment ```text The output of `python collect_env.py` ``` vLLM Version: 0.6.1.post2@9ba0817ff1eb514f51c...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: rent environment ```text The output of `python collect_env.py` ``` vLLM Version: 0.6.1.post2@9ba0817ff1eb514f51cc6de9cb8e16c98d6ee44f model: Qwen2-VL-7B-Instruct ### How would you like to use vllm My starting cmd `pytho...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
