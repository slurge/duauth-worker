from user_agents import parse
#https://github.com/selwin/python-user-agents

indexes = {
	'os' : [
		'windows 10',
		'windows 8.1',
		'windows 8',
		'windows 7',
		'windows vista',
		'windows 2003',
		'windows xp',
		'windows 2000',
		'windows nt 4.0',
		'windows nt',
		'windows 98',
		'windows 98',
		'windows 95',
		'windows 95',
		'windows phone',
		'android',
		'blackberry',
		'ios',
		'mac os x',
		'power pc mac',
		'freebsd',
		'macintosh',
		'linux',
		'debian',
		'sun solaris',
		'beos',
		'apachebench',
		'aix',
		'irix',
		'dec osf',
		'hp-ux',
		'netbsd',
		'bsdi',
		'openbsd',
		'gnu/linux',
		'unknown unix os',
		'symbian os',
		'symbian',
		'symbianos',
		'palm',
		'symbian s60',
		'windows ce'
	],
	'browsers': [
		'opera',
		'flock',
		'edge',
		'chrome',
		'internet explorer',
		'shiira',
		'firefox',
		'chimera',
		'phoenix',
		'firebird',
		'camino',
		'netscape',
		'omniweb',
		'safari',
		'mozilla',
		'konqueror',
		'icab',
		'lynx',
		'links',
		'hotjava',
		'amaya',
		'ibrowse',
		'maxthon',
		'ubuntu web browser',
		'obigo',
		'netfront browser',
		'openwave browser',
		'mobile explorer',
		'mobile safari'
		'opera mini',
		'opera mobile',
		'firefox mobile',
	],
	'devices': [
		'pc'
		'motorola',
		'nokia',
		'nexus',
		'palm',
		'iphone',
		'ipad',
		'ipod',
		'sony ericsson',
		'blackberry',
		'o2 cocoon',
		'treo',
		'lg',
		'amoi',
		'xda',
		'mda',
		'vario',
		'htc',
		'samsung',
		'sharp',
		'siemens',
		'alcatel',
		'benq',
		'hp ipaq',
		'motorola',
		'playstation portable',
		'playstation 3',
		'playstation vita',
		'danger hiptop',
		'nec',
		'panasonic',
		'philips',
		'sagem',
		'sanyo',
		'spv',
		'zte',
		'sendo',
		'nintendo dsi',
		'nintendo ds',
		'nintendo 3ds',
		'nintendo wii',
		'open web',
		'openweb',
		'meizu'
	]
}

def get_index(s, index):
	#return indexes[index].index(s.lower()) if s.lower() in indexes[index] else len(indexes[index])
	if s.lower() in indexes[index]:
		return indexes[index].index(s.lower())
	else:
		return len(indexes[index])

def parse_agent(agent):
	ua = parse(agent)
	#1 y 0 dependiendo de tipo de dispositivo
	x = [int(ua.is_pc), int(ua.is_mobile), int(ua.is_tablet), int(ua.is_touch_capable), int(ua.is_bot)]
	#datos numericos para explorador
	x += [get_index(ua.browser.family, 'browsers'), ua.browser.version[0]]
	#datos numericos para os
	x += [get_index(ua.os.family, 'os'), ua.os.version[0]]
	#datos numericos para dispositivo
	x += [get_index(ua.device.family, 'devices')]
	return x


def parse_cadence(a):
	#truncar longitud de array a 20
	if len(a) > 20:
		x = a[:20]
	elif len(a) <= 20:
		x = a + [0 for i in range(20-len(a))]
	return x


def make(cadence, agent):
	x = parse_cadence(cadence)+parse_agent(agent)
	return x


if __name__ == '__main__':
	cadence = list(range(30))
	agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
	vector = make(cadence, agent)
	print(vector)
	print(len(vector))


