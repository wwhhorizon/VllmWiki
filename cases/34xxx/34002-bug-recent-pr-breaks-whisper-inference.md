# vllm-project/vllm#34002: [Bug]: Recent PR breaks Whisper inference

| 字段 | 值 |
| --- | --- |
| Issue | [#34002](https://github.com/vllm-project/vllm/issues/34002) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 0; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;frontend_api;hardware_porting;model_support;sampling_logits;speculative_decoding |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling |
| 症状 | build_error;nan_inf |
| 根因提示 | dtype;env_dependency |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Recent PR breaks Whisper inference

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug A recent PR has broken Whisper inference. Running the producer below we see a response of just whitespace. PR: https://github.com/vllm-project/vllm/pull/31366/changes Commit: `a32cb49b60688fb64a6d3d7f86378b4d2fad06e6` ``` from vllm.assets.audio import AudioAsset from vllm import LLM, SamplingParams def main(): # prepare model llm = LLM( model="openai/whisper-large-v3", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, enforce_eager = True, ) # prepare inputs inputs = { # Test explicit encoder/decoder prompt "encoder_prompt": { "prompt": "", "multi_modal_data": { "audio": AudioAsset("winning_call").audio_and_sample_rate, }, }, "decoder_prompt": " ", } # generate response print("========== SAMPLE GENERATION ==============") outputs = llm.generate(inputs, SamplingParams(temperature=0.0, max_tokens=64)) print(f"PROMPT : {outputs[0].prompt}") print(f"RESPONSE: {outputs[0].outputs[0].text}") print("==========================================") if __name__ == "__main__": main() ``` This produces the below: ``` ========== SAMPLE GENERATION ============== Adding requests: 100%|██████████████████████████████████████████...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: : `a32cb49b60688fb64a6d3d7f86378b4d2fad06e6` ``` from vllm.assets.audio import AudioAsset from vllm import LLM, SamplingParams def main(): # prepare model llm = LLM( model="openai/whisper-large-v3", max_model_len=448, m...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: rue, ) # prepare inputs inputs = { # Test explicit encoder/decoder prompt "encoder_prompt": { "prompt": "", "multi_modal_data": { "audio": AudioAsset("winning_call").audio_and_sample_rate, }, }, "decoder
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: g_logits;speculative_decoding cuda;operator;sampling build_error;nan_inf dtype;env_dependency Your current environment
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 1: dioAsset from vllm import LLM, SamplingParams def main(): # prepare model llm = LLM( model="openai/whisper-large-v3", max_model_len=448, max_num_seqs=400, limit_mm_per_prompt={"audio": 1}, enforce_eager = True, ) # prep...

## Wiki 抽取状态

- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
