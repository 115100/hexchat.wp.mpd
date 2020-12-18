hexchat.register('MPD', '1', 'MPD currently playing script')

local function get_np()
	local handle = assert(io.popen(
			'mpc ' ..
			'current ' ..
			'-h /var/lib/mpd/socket ' ..
			'-f "%artist% - %title% 「%album%」"'
	))
	local res = string.gsub(assert(handle:read('*a')), '\n', '')
	handle:close()
	hexchat.command('SAY np: ' .. res)
	return hexchat.EAT_ALL
end

hexchat.hook_command('wp', get_np, '"/wp" to display currently playing MPD track')
hexchat.print('hexchat.wp.mpd.lua loaded')
