# vllm-project/vllm#27557: [Bug]: Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

| 字段 | 值 |
| --- | --- |
| Issue | [#27557](https://github.com/vllm-project/vllm/issues/27557) |
| 状态 | open |
| 标签 | bug |
| 评论 | 15; 本地原始数据只有评论数量，没有评论正文 |

## 源证据

### Issue 标题

> [Bug]: Engine core proc EngineCore_DP0 died unexpectedly, shutting down client.

### Issue 正文摘录

### Your current environment ### 🐛 Describe the bug ```python def load_and_encode_images(self, folder_path: str) -> List[str]: """ 从文件夹加载图像并编码为base64 :param folder_path: 图像文件夹路径 :return: 图像的base64编码列表 """ images = [] for filename in sorted(os.listdir(folder_path)): if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")): filepath = os.path.join(folder_path, filename) img = cv2.imread(filepath) if img is not None: images.append(img) return images def encode_images_to_base64(self, images: List[np.ndarray]) -> List[str]: """ 将图像列表编码为base64格式 :param images: 图像列表 :return: 图像的base64编码列表 """ encoded_images = [] for frame in images: if frame.dtype != np.uint8: frame = frame.astype(np.uint8) if len(frame.shape) == 2: frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) _, buffer = cv2.imencode('.jpg', frame) image_base64 = "data:image/jpeg;base64," + base64.b64encode(buffer).decode('utf-8') encoded_images.append(image_base64) return encoded_images encoded_images = self.encode_images_to_base64(images) messages = [ {"role": "user", "content": [{"type": "text", "text": prompt}] + [{"type": "image_url", "image_url": {"url": img}} for img in encoded_images]} ] completion = self.client.chat.c...

## 候选优化模式

- [模型格式与 Adapter 路径](../patterns/model_format_adapter.md) - 分数 2: completion = self.client.chat.completions.create( model='qwen_vl_3-2b' messages=messages, temperature=0.5, top_p=0.01, max_tokens=500 ) return completion.choices[0].message.content `
- [Dtype、量化与 Scale 路径](../patterns/dtype_quantization_path.md) - 分数 1: ed_images = [] for frame in images: if frame.dtype != np.uint8: frame = frame.astype(np.uint8) if len(frame.shape) == 2: frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR) _, buffer = cv2.imencode
- [硬件架构 Guard](../patterns/hardware_arch_guard.md) - 分数 1: ``` ### Before submitting a new issue... - [x] Make sure you already searched for relevant issues, and asked the chatbot living at the bottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), wh...
- [Scheduler 与请求状态生命周期](../patterns/scheduler_request_lifecycle.md) - 分数 1: image_base64 = "data:image/jpeg;base64," + base64.b64encode(buffer).decode('utf-8') encoded_images.append(image_base64) return encoded_images encoded_images = self.encode_images_to_base64(images) messages = [ {"role": "...
- [验证与 Benchmark](../patterns/verification_benchmarking.md) - 分数 1: ottom right corner of the [documentation page](https://docs.vllm.ai/en/latest/), which can answer lots of frequently asked questions.

## Wiki 抽取状态

- 风险：该 issue 有评论，但本地数据只有评论数量，没有评论正文。
- 该 issue 不在当前 operator/kernel case 表中；保留索引，但暂不推断优化结论。
- 后续迭代应在可用时读取完整讨论评论。
