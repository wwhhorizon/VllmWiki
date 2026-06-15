# vllm-project/vllm#19017: [Bug]:Tool calls not correctly parsed from the reasoning_content field when thinking is disabled

| 字段 | 值 |
| --- | --- |
| Issue | [#19017](https://github.com/vllm-project/vllm/issues/19017) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 5; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]:Tool calls not correctly parsed from the reasoning_content field when thinking is disabled

### Issue 正文摘录

### Your current environment Running model [Qwen3-32B-FP8](https://huggingface.co/Qwen/Qwen3-32B-FP8) on `vllm-openai:v0.9.0.1` docker image with following flags: ``` --tensor-parallel-size 1 --max-model-len 28000 --gpu-memory-utilization 0.90 --enable-auto-tool-choice --tool-call-parser hermes --enable-reasoning --reasoning-parser deepseek_r1 ``` ### 🐛 Describe the bug Tool calls not correctly parsed from the `reasoning_content` field **when thinking is disabled.** To reproduce: ```python SYSTEM_PROMPT = "You are a helpful assistant." USER_PROMPT = "In one short sentence, greet the world!" FUNCTIONS_SCHEMA = [{ "name": "greet_world", "description": "Returns a single sentence to greet the world.", "parameters": {"type": "object", "properties": {}, "required": []}, }] def run_completion( client: OpenAI, *, model: str, stream: bool, with_funcs: bool, disable_thinking: bool, timeout: int, ): label = ( f"{'stream' if stream else 'sync'}" + ("/func" if with_funcs else "") + ("/thinkOFF" if disable_thinking else "") ) print(f" ↳ {label} …") kwargs = dict( model=model, messages=[ {"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": f"{USER_PROMPT}. Use tools if possi...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 4: ield when thinking is disabled bug ### Your current environment Running model [Qwen3-32B-FP8](https://huggingface.co/Qwen/Qwen3-32B-FP8) on `vllm-openai:v0.9.0.1` docker image with following flags: ``` --tensor-parallel...
- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 2: P8](https://huggingface.co/Qwen/Qwen3-32B-FP8) on `vllm-openai:v0.9.0.1` docker image with following flags: ``` --tensor-parallel-size 1 --max-model-len 28000 --gpu-memory-utilization 0.90 --enable-auto-tool-choice --to...
- [Bitwise 确定性与数值等价](../patterns/bitwise_determinism_equivalence.md) - 分数 1: ed from the `reasoning_content` field **when thinking is disabled.** To reproduce: ```python SYSTEM_PROMPT = "You are a helpful assistant." USER_PROMPT = "In one short sentence, greet the world!" FUNCTIONS_SCHEMA = [{ "...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g is disabled bug ### Your current environment Running model [Qwen3-32B-FP8](https://huggingface.co/Qwen/Qwen3-32B-FP8) on `vllm-openai:v0.9.0.1` docker image with following flags: ``` --tensor-parallel-size 1 --max-mod...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
