# vllm-project/vllm#16953: [Bug]: Fail to use deepseek vl2 with images, maybe need a new chat template?

| 字段 | 值 |
| --- | --- |
| Issue | [#16953](https://github.com/vllm-project/vllm/issues/16953) |
| 状态 | closed |
| 标签 | bug;stale |
| 评论 | 6; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Fail to use deepseek vl2 with images, maybe need a new chat template?

### Issue 正文摘录

### Your current environment transformers 4.49.0 vllm 0.7.3 huggingface-hub 0.29.3 pytorch-quantization 2.1.2 torch 2.5.1 torch-tensorrt 2.2.0a0 torchaudio 2.5.1 torchdata 0.7.0a0 torchtext 0.17.0a0 torchvision 0.20.1 model: deepseek-vl2-small ### 🐛 Describe the bug I use vllm to start a model server. My start command is ``` python -m vllm.entrypoints.openai.api_server \ --model {MY_MODEL_PATH} \ --host 0.0.0.0 \ --port 8000 \ --api-key {MY_API_KEY} \ --served-model-name deepseek_vl2_small \ --limit-mm-per-prompt "image=2" \ --hf-overrides '{"architectures": ["DeepseekVLV2ForCausalLM"]}' \ --chat_template ./template_deepseek_vl2.jinja ``` chat template is [template_deepseek_vl2.jinja](https://github.com/vllm-project/vllm/pull/12143/files#diff-34c8e1d46b0ef913c369929c81253209c4c7800b6f7a86d32135b8138a3e34ca) request code: ``` client = OpenAI( api_key={MY_API_KEY}, base_url={MODEL_URL} ) models = client.models.list() model_id = models.data[0].id with open(file_path, "rb") as image_file: encoded = base64.b64encode(image_file.read()).decode('utf-8') completion = client.chat.completions.create( max_tokens=512, temperature=0.5, top_p=0.3, model=model_id, messages=[ { "role": "user", "co...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 3: 4.49.0 vllm 0.7.3 huggingface-hub 0.29.3 pytorch-quantization 2.1.2 torch 2.5.1 torch-tensorrt 2.2.0a0 torchaudio 2.5.1 torchdata
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 3: ail to use deepseek vl2 with images, maybe need a new chat template? bug;stale ### Your current environment transformers 4.49.0 vllm 0.7.3 huggingface-hub 0.29.3 pytorch-quantization 2.1.2 torch
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 2: .17.0a0 torchvision 0.20.1 model: deepseek-vl2-small ### 🐛 Describe the bug I use vllm to start a model server. My start command is ``` python -m vllm.entrypoints.openai.api_server \ --model {MY_MODEL_PATH} \ --host 0.0...
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: 0.7.3 huggingface-hub 0.29.3 pytorch-quantization 2.1.2 torch 2.5.1 torch-tensorrt 2.2.0a0 torchaudio 2.5.1 torchdata 0.7.0a0 torchtext

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
