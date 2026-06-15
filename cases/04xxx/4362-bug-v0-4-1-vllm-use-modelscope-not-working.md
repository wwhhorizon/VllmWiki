# vllm-project/vllm#4362: [Bug]: v0.4.1 VLLM_USE_MODELSCOPE not working

| 字段 | 值 |
| --- | --- |
| Issue | [#4362](https://github.com/vllm-project/vllm/issues/4362) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 8; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: v0.4.1 VLLM_USE_MODELSCOPE not working

### Issue 正文摘录

### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug the related code in the previous version : `if os.environ.get("VLLM_USE_MODELSCOPE", "False").lower() == "true":` now the code: `if VLLM_USE_MODELSCOPE:` but the `VLLM_USE_MODELSCOPE` is set to string "true" by ``` VLLM_USE_MODELSCOPE = os.environ.get("VLLM_USE_MODELSCOPE", "False").lower() == "true" ``` so, VLLM_USE_MODELSCOPE will never work

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 1: ct_env.py` ``` ### 🐛 Describe the bug the related code in the previous version : `if os.environ.get("VLLM_USE_MODELSCOPE", "False").lower() == "true":` now the code: `if VLLM_USE_MODELSCOPE:` but the `VLLM_USE_MODELSCOP...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 1: in the previous version : `if os.environ.get("VLLM_USE_MODELSCOPE", "False").lower() == "true":` now the code: `if VLLM_USE_MODELSCOPE:` but the `VLLM_USE_MODELSCOPE` is set to string "true" by ``` VLLM_USE_MODELSCOPE =...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: [Bug]: v0.4.1 VLLM_USE_MODELSCOPE not working bug ### Your current environment ```text The output of `python collect_env.py` ``` ### 🐛 Describe the bug the related code in the previous version : `if os.environ.get("VLLM...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
