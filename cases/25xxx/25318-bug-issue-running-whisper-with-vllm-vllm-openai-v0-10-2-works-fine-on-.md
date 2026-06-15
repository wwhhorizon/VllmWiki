# vllm-project/vllm#25318: [Bug]: Issue Running Whisper with vllm/vllm-openai:v0.10.2 (Works Fine on v0.10.1)

| 字段 | 值 |
| --- | --- |
| Issue | [#25318](https://github.com/vllm-project/vllm/issues/25318) |
| 状态 | closed |
| 标签 | bug |
| 评论 | 7; 本地原始数据只有评论数量，没有评论正文 |
| 一级分类 | correctness |
| 工作域 | ci_build;distributed_parallel;frontend_api;hardware_porting;model_support;sampling_logits |
| 子分类 | precision |
| Operator 关键词 | cuda;operator;sampling;triton |
| 症状 | build_error;crash;nan_inf |
| 根因提示 | dtype;env_dependency;memory_layout |
| 硬件范围 | amd;nvidia |
| 需要人工复核 | False |

## 源证据

### Issue 标题

> [Bug]: Issue Running Whisper with vllm/vllm-openai:v0.10.2 (Works Fine on v0.10.1)

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug I tried serving the Whisper model, but whenever I send the following request, I encounter an error. Moreover, the request seems to bring the whole model down. ``` audio_file_path = file_path + "/../data/test_files/d6_10_20_17-625ddc96edfd375a7cbfa57189dfb064-2905E5.wav" openai_api_key = "EMPTY" openai_api_base = "http://0.0.0.0:8000/v1" client = OpenAI(api_key=openai_api_key, base_url=openai_api_base) sync_openai(audio_file_path, client) def sync_openai(audio_file_path: str, client: OpenAI): t1 = time.time() with open(audio_file_path, "rb") as f: transcription = client.audio.transcriptions.create( file=f, model="whisper", language="fa", response_format="json", temperature=0.0, # Additional sampling params not provided by OpenAI API. extra_body=dict( seed=4419, # repetition_penalty=1.3, ), ) t2 = time.time() print(t2-t1) print("transcription result:", transcription.text) ``` In a way, this request acts like a "kill request" for the model. I’m running Docker with the image vllm/vllm-openai:v0.10.2 and I serve the model using the following command: ``` vllm serve /app/data/asr/whisper \ --gpu-memory-utilization 0.06 \ --dtype bfloat...

## 候选优化模式

- [构建、依赖与打包](../patterns/build_dependency_packaging.md) - 分数 4: way, this request acts like a "kill request" for the model. I’m running Docker with the image vllm/vllm-openai:v0.10.2 and I serve the model using the following command: ``` vllm serve /app/data/asr/whisper \ --gpu-memo...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 3: vllm serve /app/data/asr/whisper \ --gpu-memory-utilization 0.06 \ --dtype bfloat16 \ --block-size 16 \ --max-num-seqs 32 \ --served-model-name whisper \ --middleware src.timing_middleware.log_timing_middleware ``` The...
- [Metadata 与 Layout 契约](../patterns/metadata_layout_contract.md) - 分数 3: asr/whisper \ --gpu-memory-utilization 0.06 \ --dtype bfloat16 \ --block-size 16 \ --max-num-seqs 32 \ --served-model-name whisper \ --middleware src.timing_middleware.log_timing_middleware ``` The client throws the fol...
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: es. ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: rent environment ### 🐛 Describe the bug I tried serving the Whisper model, but whenever I send the following request, I encounter an error. Moreover, the request seems to bring the whole model down. ``` audio_file_path...

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 本地没有 linked-fix 证据；目前只支持症状/路径抽取。
- 后续迭代应在可用时读取完整讨论评论。
