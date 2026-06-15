# vllm-project/vllm#22519: [Bug]: [gpt oss 20b] [tool_call] Unexpected token 12606 while expecting start token 200006

| 字段 | 值 |
| --- | --- |
| Issue | [#22519](https://github.com/vllm-project/vllm/issues/22519) |
| 状态 | open |
| 标签 | bug;gpt-oss |
| 评论 | 38; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: [gpt oss 20b] [tool_call] Unexpected token 12606 while expecting start token 200006

### Issue 正文摘录

### Your current environment uv venv --python 3.12 --seed source .venv/bin/activate uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/cu128 \ --index-strategy unsafe-best-match vllm serve openai/gpt-oss-20b ### 🐛 Describe the bug It looks like there's a problem with gpt-oss-20b when using tool_call. The model is throwing the following error: openai_harmony.HarmonyError: Unexpected token 12606 while expecting start token 200006 This happens after the model returns token 200012. Token 12606 corresponds to the word "comment". I suspect the model intended to return the special token for "commentary" but instead returned a split version, "comment" and "ary". This issue does not occur with gpt-oss-120b, which works as expected.

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: vironment uv venv --python 3.12 --seed source .venv/bin/activate uv pip install --pre vllm==0.10.1+gptoss \ --extra-index-url https://wheels.vllm.ai/gpt-oss/ \ --extra-index-url https://download.pytorch.org/whl/nightly/...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: tool_call] Unexpected token 12606 while expecting start token 200006 bug;gpt-oss ### Your current environment uv venv --python 3.12 --seed source .venv/bin/activate uv pip install --pre vllm==0.10.1+gptoss \ --extra-ind...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
